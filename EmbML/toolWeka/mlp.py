
import javaobj
import math
import sys

# Need to be adjusted when the model is too large
sys.setrecursionlimit(10000)

if len(sys.argv) < 3:
    print "Usage: python " + sys.argv[0] + " <modelFile> <destinationFile> [-opts]"
    print "\nOptions:\n\t-fxp <n> <m>:  use fixed point Qn.m representation in all calculations\n"
    exit(0)

#######################################################################################################
# HANDLING FIXED POINT OPTION

useFxp = ('-fxp' in sys.argv)

totalBits = 0
fixedBits = 0

if useFxp:
    if len(sys.argv) <= sys.argv.index('-fxp') + 2:
        print "Error: define values for n and m"
        exit(0)
        
    fixedBits = int(sys.argv[sys.argv.index('-fxp') + 2])
    totalBits = int(sys.argv[sys.argv.index('-fxp') + 1]) + fixedBits + 1

    if totalBits != 8 and totalBits != 16 and totalBits != 32:
        print "Error: n + m needs to be equals to 7, 15, or 31"
        exit(0)

#######################################################################################################
# OPENING MODEL FILE

try: file = open(sys.argv[2], "w")
except:
    print "Error: destination file invalid"
    exit()

try: modelFile = open(sys.argv[1])
except:
    print "Error: model file invalid"
    exit()

marshaller = javaobj.JavaObjectUnmarshaller(modelFile)
obj = marshaller.readObject()

#######################################################################################################

# Convert a float point number to its fixed point representation
# returns a string that has this representation in hexidecimal.
def toFxp(x):
    if totalBits == 32:
        return "(FixedNum)0x%.8x" % (int(round(x * (1 << fixedBits))) & 0xFFFFFFFF)
    if totalBits == 16:
        return "(FixedNum)0x%.4x" % (int(round(x * (1 << fixedBits))) & 0xFFFF)
    if totalBits == 8:
        return "(FixedNum)0x%.2x" % (int(round(x * (1 << fixedBits))) & 0xFF)

def chooseDataType(v):
    if max(v) <= 127 and min(v) >= -128: return "int8_t"
    if max(v) <= 255 and min(v) >= 0: return "uint8_t"
    if max(v) <= 32767 and min(v) >= -32768: return "int16_t"
    if max(v) <= 65535 and min(v) >= 0: return "uint16_t"
    if max(v) <= 2147483647 and min(v) >= -2147483648: return "int32_t"
    if max(v) <= 4294967295 and min(v) >= 0: return "uint32_t"
    if max(v) <= 9223372036854775807 and min(v) >= -9223372036854775808: return "int64_t"
    if max(v) <= 18446744073709551615 and min(v) >= 0: return "uint64_t"
    else: return "int64_t"

#######################################################################################################

ids = dict()
idsOut = dict()
idsIn = dict()
sigIds = dict()

classIndex = vars(vars(obj)['m_instances'])['m_ClassIndex']

# define an id for each neuron
def setIds(obj, cte):
    if type(obj) != javaobj.JavaObject or\
       'NeuralEnd' in str(obj) or\
       ids.has_key(vars(obj)['m_id']): return

    for i in vars(obj)['m_inputList']:
        if type(i) == javaobj.JavaObject:
            setIds(i, cte)
            
    ids[vars(obj)['m_id']] = len(ids) + cte
    
    if 'SigmoidUnit' in str(vars(obj)['m_methods']):
        sigIds[ids[vars(obj)['m_id']]] = True

# build the graph for the neural network
def buildGraph(obj, weights, visited):
    if type(obj) != javaobj.JavaObject or\
       'NeuralEnd' in str(obj): return 

    m_inputList = vars(obj)['m_inputList']
    m_id = ids[vars(obj)['m_id']]
    m_weights = vars(obj)['m_weights']

    if visited[m_id]: return
    visited[m_id] = True
    weights[m_id].append((-1,m_weights[0])) # -1 means bias

    for i in range(len(m_inputList)):
        if type(m_inputList[i]) != javaobj.JavaObject:
            continue
        
        if 'NeuralEnd' in str(m_inputList[i]):
            idNext = idsIn[vars(m_inputList[i])['m_id']]
        else:
            idNext = ids[vars(m_inputList[i])['m_id']]
            
        buildGraph(m_inputList[i], weights, visited)
        weights[m_id].append((idNext,m_weights[i+1]))

m_outputs = vars(obj)['m_outputs']
m_inputs = vars(obj)['m_inputs']

# First, set ids for neurons in input layer
for node in m_inputs:
    if not idsIn.has_key(vars(node)['m_id']):
        idsIn[vars(node)['m_id']] = len(idsIn)

# Second, set ids for neurons in hidden layers
for node in m_outputs:
    for c in vars(node)['m_inputList']:
        setIds(c, len(idsIn))

# Last, set ids for neurons in output layer
for node in m_outputs:
    if not idsOut.has_key(vars(node)['m_id']):
        idsOut[vars(node)['m_id']] = len(idsOut) + len(ids) + len(idsIn)

weights = [[] for _ in range(len(ids) + len(idsOut) + len(idsIn))]
visited = [False for _ in range(len(weights))]

# Recover weights for each neuron
for node in m_outputs:
    m_id = idsOut[vars(node)['m_id']]
    weights[m_id].append((-1,0)) # bias
    
    for c in vars(node)['m_inputList']:
        if type(c) != javaobj.JavaObject:
            continue
        
        buildGraph(c, weights, visited)
        idNext = ids[vars(c)['m_id']]
        weights[m_id].append((idNext,1))

m_attributeBases = vars(obj)['m_attributeBases']
m_attributeRanges = vars(obj)['m_attributeRanges']

m_attributeBases.pop(classIndex)
m_attributeRanges.pop(classIndex)

#######################################################################################################
# Write the classifier file

funcs = ""
decls = ""
inits = "\n"
defs = ""
incls = "\n"

################################ FUNCTIONS ################################

### calculateOutput function
funcs += "\n\
/* Function calculateOutput description:\n\
 * Returns the output value from a neuron\n\
 */\ninline void calculateOutput(){\n\
\tfor (int i = 0; i < INPUT_SIZE; i++){\n\
\t\tm_value[i] = instance[i];\n\
\t}\n\
\n\
\tfor (int i = INPUT_SIZE; i < NUMBER_OF_NEURONS; i++){\n\
\t\t" + ("FixedNum" if useFxp else "float") + " value = m_weights[m_indicesMap[i] + (i - INPUT_SIZE)];\n\
\t\tfor (int j = 0; j < (m_indicesMap[i + 1] - m_indicesMap[i]); j++){\n\
\t\t\tvalue " +\
("= fxp_sum(value, fxp_mul(m_weights[m_indicesMap[i] + (i - INPUT_SIZE) + j + 1],\
 m_value[m_connections[m_indicesMap[i]] + j]));" if useFxp \
 else "+= m_weights[m_indicesMap[i] + (i - INPUT_SIZE) + j + 1] * m_value[m_connections[m_indicesMap[i]] + j];") + "\n\
\t\t}\n\
\t\tif (sigmoids[i]){\n"

funcs += "\t\t\tif (value < " +\
         (toFxp(-45.0) if useFxp else "-45.0") + ")\n\
\t\t\t\tvalue = " + ("(FixedNum)0" if useFxp else "0.0") + ";\n\
\t\t\telse if (value > " + (toFxp(45.0) if useFxp else "45.0") + ")\n\
\t\t\t\tvalue = " + (toFxp(1.0) if useFxp else "1.0") + ";\n\
\t\t\telse{\n\
\t\t\t\tvalue = " +\
(("fxp_div(" + toFxp(1.0) + ", fxp_sum(" + toFxp(1.0) +\
  ", fxp_exp(-value)));\n") if useFxp else\
 "1.0 / (1.0 + exp(-value));\n")
    
funcs += "\t\t\t}\n\
\t\t}\n\
\t\tm_value[i] = value;\n\
\t}\n\
}\n"

funcs += "\n\
/* Function classify description:\n\
 * Instance array must be initializated, with\
 appropriated attributes, before calling this function\n"

outputs = []
for i in idsOut:
    funcs += " * Output number "\
             + str(len(outputs))\
             + " means that the instance was classified as \'"\
             + str(i)\
             + "\'\n"
    outputs.append(idsOut[i])
funcs += " */\n"

### classify function
funcs += "int classify(){\n\
\t" + ("FixedNum" if useFxp else "float") + " theArray[OUTPUT_SIZE];\n\
\tfor (int i = 0; i < INPUT_SIZE; i++){\n\
\t\tif (m_attributeRanges[i] != " +\
("(FixedNum)0" if useFxp else "0") + "){\n\
\t\t\tinstance[i] = " + \
("fxp_div(fxp_diff(instance[i], m_attributeBases[i]), m_attributeRanges[i]);"\
 if useFxp else\
 "(instance[i] - m_attributeBases[i]) / m_attributeRanges[i];") + "\n\
\t\t}\n\
\t\telse{\n\
\t\t\tinstance[i] = " + \
("fxp_diff(instance[i], m_attributeBases[i]);" if useFxp \
 else "(instance[i] - m_attributeBases[i]);") + "\n\
\t\t}\n\
\t}\n\
\tcalculateOutput();\n\
\tfor (int i = 0; i < OUTPUT_SIZE; i++){\n\
\t\ttheArray[i] = m_value[m_outputs[i]];\n\
\t}\n\
\t" + ("FixedNum" if useFxp else "float") + " maxValue = " +\
("-1" if useFxp else "-1.0") + ";\n\
\tint indexMax = -1;\n\
\tfor (int i = 0; i < OUTPUT_SIZE; i++){\n\
\t\tif (theArray[i] > maxValue){\n\
\t\t\tmaxValue = theArray[i];\n\
\t\t\tindexMax = i;\n\
\t\t}\n\
\t}\n\
\treturn indexMax;\n\
}\n"

################################ DECLARATIONS ################################

inputs = []
for i in idsIn:
    inputs.append((idsIn[i],i))
inputs.sort()

### print sorted attributes
decls += "\n/* Instance array must be global\n\
 * Attributes MUST be sorted in instance array in the following order:\n"

for i,j in inputs:
    decls += " * " + str(j) + "\n"
decls += " */\n"

### instance array
decls += ("FixedNum" if useFxp else "float")\
         + " instance[INPUT_SIZE+1];\n"

### m_outputs array
decls += "\nconst " + chooseDataType(outputs) + " m_outputs[OUTPUT_SIZE] = {"\
         + str(outputs).replace(']','').replace('[','')\
         + "};\n"

### m_attributeBases array
decls += "\nconst " + ("FixedNum" if useFxp else "float")\
         + " m_attributeBases[INPUT_SIZE] = {"\
         + str([toFxp(i) if useFxp else\
                str(i) for i in m_attributeBases]).replace(']','').\
                replace('[','').replace('\'','')\
         + "};\n"

### m_attributeRanges array
decls += "const " + ("FixedNum" if useFxp else "float")\
         + " m_attributeRanges[INPUT_SIZE] = {"\
         + str([toFxp(i) if useFxp else\
                str(i) for i in m_attributeRanges]).replace(']','').\
                replace('[','').replace('\'','')\
         + "};\n"

inits += "void initConnections(){\n"

### initialize m_connections and m_weights arrays
m_connections = []
m_weights = []
m_indicesMap = [0]
for i in range(len(weights)):

    if len(weights[i]) == 0:
        # case in which neurons are connected to nothing (input neurons)
        m_indicesMap.append(m_indicesMap[-1])
        continue

    wei = []
    con = []
    for j,k in weights[i]:
        if j == -1:
            # bias is the first number in array wei
            wei.insert(0, k)
            continue
        wei.append(k)
        con.append(j)

    # number of connections is the first number in array con
    # con.insert(0,len(con))
    
    m_indicesMap.append(len(con) + m_indicesMap[-1])
    m_connections += con
    m_weights += wei

### m_weights array
decls += "\nconst " + ("FixedNum" if useFxp else "float")\
         + " m_weights[" + str(len(m_weights)) + "] = " +\
         str([toFxp(_i) for _i in m_weights]\
             if useFxp else \
             m_weights).replace('[','{').replace(']','}').replace('\'','') + ";\n"
decls += "const " + chooseDataType(m_connections) + " m_connections[" + str(len(m_connections)) + "] = " + str(m_connections).replace('[','{').replace(']','}') + ";\n"
decls += "const " + chooseDataType(m_indicesMap) + " m_indicesMap[" + str(len(m_indicesMap)) + "] = " + str(m_indicesMap).replace('[','{').replace(']','}') + ";\n"

inits += "}\n"

sigmoids = []
for i in range(len(weights)):
    if sigIds.has_key(i):
        sigmoids.append(True)
    else:
        sigmoids.append(False)

### sigmoids array
decls += "\nconst bool sigmoids[NUMBER_OF_NEURONS] = {"\
         + str(sigmoids).lower().replace(']','').replace('[','')\
         + "};\n"

### m_value array
decls += "\n" + ("FixedNum" if useFxp else "float") + " m_value[NUMBER_OF_NEURONS];\n"
decls += "\n/* Before every classification, all elements \
in m_calculated array need to be set to false */" +\
"\nbool m_calculated[NUMBER_OF_NEURONS];\n"

################################ DEFINES ################################

defs += "\n#define INPUT_SIZE " + str(len(inputs))\
        + "\n#define CLASS_INDEX " + str(classIndex)\
        + "\n#define OUTPUT_SIZE " + str(len(outputs))\
        + "\n#define NUMBER_OF_NEURONS " + str(len(weights))\
        + "\n"

################################ INCLUDES ################################

incls += "#include <Arduino.h>\n"\
         + (("#define TOTAL_BITS " + str(totalBits) +\
             "\n#define FIXED_FBITS " + str(fixedBits) +\
             "\n#define SIGNED" +\
             "\n#include \"FixedNum.h\"\n") if useFxp else "")\
         + ("\n" if useFxp else "#include <math.h>\n\n")

file.write(incls)
file.write(defs)
file.write(decls)
file.write(funcs)
file.write(inits)

file.close()
