
import javaobj
import math
import sys

if len(sys.argv) < 3:
    print "Usage: python " + sys.argv[0] + " <modelFile> <destinationFile> [-opts]"
    print "\nOptions:\n\t-fxp <n> <m>:  use fixed point Qn.m representation in all calculations\n"
    exit()

useFxp = ('-fxp' in sys.argv)
useDivMul = ('-div-mul' in sys.argv)

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
    print "Destination file invalid"
    exit()

try: modelFile = open(sys.argv[1])
except:
    print "Model file invalid"
    exit()

marshaller = javaobj.JavaObjectUnmarshaller(modelFile)
obj = marshaller.readObject()

#######################################################################################################


# Convert a float point number to its fixed point representation
# returns a string that has this representation in hexidecimal.
def toFxp(x):
    if math.isnan(x):
        return "INF_POS"
    if totalBits == 32:
        return "(FixedNum)0x%.8x" % (int(round(x * (1 << fixedBits))) & 0xFFFFFFFF)
    if totalBits == 16:
        return "(FixedNum)0x%.4x" % (int(round(x * (1 << fixedBits))) & 0xFFFF)
    if totalBits == 8:
        return "(FixedNum)0x%.2x" % (int(round(x * (1 << fixedBits))) & 0xFF)

def chooseDataType(v):
    if not 'list' in str(type(v)) and not 'array' in str(type(v)):
        v = [v]
        
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
    
# hashtable = nome da classe -> valor
classesNumbers = vars(vars(vars(vars(obj)['m_classAttribute'])['m_AttributeInfo'])['m_Hashtable'])['annotations'][1:]

# quantidade de classes
m_numClasses = vars(vars(vars(vars(obj)['m_classAttribute'])['m_AttributeInfo'])['m_Values'])['size']

# indice da classe (0-indexed)
m_classIndex = vars(obj)['m_classIndex']

# atributos e indices
atts = vars(vars(vars(vars(vars(obj)['m_Filter'])['m_InputRelAtts'])['m_Data'])['m_NamesToAttributeIndices'])['annotations'][1:]
inputs = ['' for _ in range(len(atts)/2-1)]
for i in range(len(atts)/2):
    if 'String' in str(type(atts[2*i])) and m_classIndex != vars(atts[2*i+1])['value']:
        inputs[int(vars(atts[2*i+1])['value'])] = atts[2*i]
        
outputs = []
className = "class"
for i in classesNumbers:
    if 'String' in str(type(i)): className = str(i)
    else: outputs.append((vars(i)['value'], className))
outputs.sort()

minArray = vars(vars(obj)['m_Filter'])['m_MinArray']
maxArray = vars(vars(obj)['m_Filter'])['m_MaxArray']
m_KernelIsLinear = vars(obj)['m_KernelIsLinear']
m_classifiers = vars(obj)['m_classifiers']

new_classifiers = [[] for _ in m_classifiers]
for i in range(len(m_classifiers)):
    for j in range(len(m_classifiers[i])):
        if "None" in str(type(m_classifiers[i][j])): continue
        new_classifiers[j].append(m_classifiers[i][j])

m_gamma = vars(vars(new_classifiers[1][0])['m_kernel'])['m_gamma']

funcs = "\n"
decls = "\n"
inits = "\n"
defs = "\n"
incls = "\n"

################################ FUNCTIONS ################################

              
funcs += "\n" + ("FixedNum" if useFxp else "float") + " SVMOutput(int i, int j){\n\
\t" + ("FixedNum" if useFxp else "float") + " result = " + (toFxp(0) if useFxp else "0.0") + ";\n\
\tfor (int k = 0; k < (m_size[i][j] - (j == 0 ? 0 : m_size[i][j-1])); k++){\n\
\t\t" + ("FixedNum" if useFxp else "float") + " resultAux = " + (toFxp(0) if useFxp else "0.0") + ";\n\
\t\tfor (int p1 = 0; p1 <= INPUT_SIZE; p1++){\n\
\t\t\tif (p1 != CLASS_INDEX){\n\
\t\t\t\tresultAux " + ("= fxp_sum(resultAux, fxp_mul(fxp_diff(instance[p1], m_AttValues[i][j][(k * (INPUT_SIZE + 1)) + p1]), fxp_diff(instance[p1], m_AttValues[i][j][(k * (INPUT_SIZE + 1)) + p1])))" if useFxp else\
                    "+= (instance[p1] - m_AttValues[i][j][(k * (INPUT_SIZE + 1)) + p1]) * (instance[p1] - m_AttValues[i][j][(k * (INPUT_SIZE + 1)) + p1])") + ";\n\
\t\t\t}\n\
\t\t}\n\
\t\tresultAux = " + (("fxp_exp(fxp_mul(-M_GAMMA, resultAux))") if useFxp else\
                     "exp(-M_GAMMA * resultAux)")\
              + ";\n\
\t\tresult " + ("= fxp_sum(result, fxp_mul(m_class_alpha[i][(j == 0 ? 0 : m_size[i][j - 1]), resultAux))" if useFxp else\
                "+= m_class_alpha[i][(j == 0 ? 0 : m_size[i][j - 1]) * resultAux")\
                + ";\n\
\t}\n\
\tresult " + ("= fxp_diff(result, m_b[i][j])" if useFxp\
              else "-= m_b[i][j]") + ";\n\
\treturn result;\n\
}\n"

funcs += "\n/* Function classify description:\n * Instance array must be initializated, with appropriated attributes, before calling this function\n"

for i,j in outputs:
    funcs += " * Output number " + str(i) + " means that the instance was classified as " + j + "\n"
funcs += " */\n"
funcs += "int classify(){\n\
\tfor (int i = 0; i < INPUT_SIZE; i++){\n\
\t\tif (" + ("rangeArray[i] == 0" if useDivMul else "maxArray[i] == minArray[i]") + " || minArray[i] == " + ("INF_POS" if useFxp else "NAN") + "){\n\
\t\t\tinstance[i] = " + ("(FixedNum)" if useFxp else "") + "0;\n\
\t\t}\n\
\t\telse{\n\
\t\t\tinstance[i] = " +\
("fxp_" + ("mul" if useDivMul else "div") + "(fxp_diff(instance[i], minArray[i]), " + ("rangeArray[i]" if useDivMul else "fxp_diff(maxArray[i], minArray[i])") + ");" if useFxp\
 else "(instance[i] - minArray[i]) / (maxArray[i] - minArray[i]);") + "\n\
\t\t}\n\
\t}\n\
\tint result[NUM_CLASSES] = {0};\n\
\tfor (int i = 1; i < NUM_CLASSES; i++){\n\
\t\tfor (int j = 0; j < i; j++){\n\
\t\t\t" + ("FixedNum" if useFxp else "float") + " output = SVMOutput(i, j);\n\
\t\t\tif (output > 0){\n\
\t\t\t\tresult[i]++;\n\
\t\t\t}\n\
\t\t\telse{\n\
\t\t\t\tresult[j]++;\n\
\t\t\t}\n\
\t\t}\n\
\t}\n\
\tint indMax = 0;\n\
\tfor (int i = 1; i < NUM_CLASSES; i++){\n\
\t\tif (result[i] > result[indMax]){\n\
\t\t\tindMax = i;\n\
\t\t}\n\
\t}\n\
\treturn indMax;\n\
}\n"

################################ DECLARATIONS ################################

decls += "/* Instance array must be global\n * Attributes MUST be sorted in instance array in the following order:\n"
for i in inputs:
    decls += " * " + i + "\n"
decls += " */\n" + ("FixedNum" if useFxp else "float") + " instance[INPUT_SIZE+1];\n"

sizeMinArray = len(minArray)
sizeMaxArray = len(maxArray)
rangeArray = []

if useDivMul:
    for i in range(len(inputs)):
        if math.isnan(maxArray[i]) or maxArray[i] == minArray[i]:
            rangeArray.append(0)
        else:
            rangeArray.append(1.0 / float(maxArray[i] - minArray[i]))
            
if useFxp:
    minArray = [toFxp(_i) for _i in minArray]
    maxArray = [toFxp(_i) for _i in maxArray]
    rangeArray = [toFxp(_i) for _i in rangeArray]

minArray = (str(minArray).replace('\'','') if useFxp else str(minArray).upper())
maxArray = str(maxArray).replace('\'','')
rangeArray = str(rangeArray).replace('\'','')

decls += "const " + ("FixedNum" if useFxp else "float") + " minArray[" + str(sizeMinArray) + "] = " + minArray.replace('[','{').replace(']','}') + ";\n"

if useDivMul:
    sizeRangeArray = len(rangeArray)
    decls += "const " + ("FixedNum" if useFxp else "float") + " rangeArray[" + str(sizeMaxArray) + "] = " + rangeArray.replace('[','{').replace(']','}') + ";\n"
else:
    decls += "const " + ("FixedNum" if useFxp else "float") + " maxArray[" + str(sizeMaxArray) + "] = " + maxArray.replace('[','{').replace(']','}') + ";\n"

decls += "\n"

inits += "void initConnections(){\n"

#vars(binarySMO)['m_class'] 1d
m_class = []

for i in range(len(new_classifiers)):
    m_class.append([])
    
    if len(new_classifiers[i]) == 0:
        continue
    
    for j in range(len(new_classifiers[i])):
        m_class[i].append(vars(new_classifiers[i][j])['m_class'])

#vars(binarySMO)['m_alpha'] 1d
decls += "\nconst " + ("FixedNum" if useFxp else "float") + " *m_class_alpha[" + str(len(new_classifiers)) + "];\n"

selectedIndices = []

for i in range(len(new_classifiers)):
    selectedIndices.append([])
    
    if len(new_classifiers[i]) == 0:
        inits += "\n\tm_class_alpha[" + str(i) + "] = NULL;\n\n"
        continue

    m_class_alpha = []
    for j in range(len(new_classifiers[i])):
        selectedIndices[i].append([])

        rawArray = vars(new_classifiers[i][j])['m_alpha']

        for k in range(len(rawArray)):
            rawArray[k] = (rawArray[k] * m_class[i][j][k])
            if rawArray[k] != 0.0:
                selectedIndices[i][j].append(k)
        array = []
        for k in selectedIndices[i][j]:
            array.append(rawArray[k])
            
        if useFxp:
            array = [toFxp(_i) for _i in array]

        m_class_alpha += array
            
    decls += "\nconst " + ("FixedNum" if useFxp else "float") + " tmp0_class_alpha" + str(i) + "[" + str(len(m_class_alpha)) + "] = " + str(m_class_alpha).replace(']','}').replace('[','{').replace('\'','') + ";\n"
    inits += "\tm_class_alpha[" + str(i) + "] = tmp0_class_alpha" + str(i) + ";\n\n"

# number of instances used
decls += "\nconst int *m_size[" + str(len(new_classifiers)) + "];\n"

for i in range(len(selectedIndices)):
    if len(selectedIndices[i]) == 0:
        inits += "\n\tm_size[" + str(i) + "] = NULL;\n\n"
        continue
    array = [len(_j) for _j in selectedIndices[i]]
    for _j in range(1,len(array)):
        array[_j] += array[_j - 1]
    decls += "\nconst int tmp_size" + str(i) + "[" + str(len(selectedIndices[i])) + "] = " + str(array).replace(']','}').replace('[','{').replace('\'','') + ";\n"
    inits += "\tm_size[" + str(i) + "] = tmp_size" + str(i) + ";\n\n"

#vars(vars(vars(vars(vars(binarySMO)['m_kernel'])['m_data'])['m_Instances'])['annotations'][1:][X])['m_AttValues'] 2d
decls += "\nconst " + ("FixedNum" if useFxp else "float") + " **m_AttValues[" + str(len(new_classifiers)) + "];\n"

for i in range(len(new_classifiers)):
    if len(new_classifiers[i]) == 0:
        inits += "\n\tm_AttValues[" + str(i) + "] = NULL;\n\n"
        continue
    decls += "\nconst " + ("FixedNum" if useFxp else "float") + " *tmp0_AttValues" + str(i) + "[" + str(len(new_classifiers[i])) + "];\n"
    for j in range(len(new_classifiers[i])):

        rawMatrix = vars(vars(vars(vars(new_classifiers[i][j])['m_kernel'])['m_data'])['m_Instances'])['annotations'][1:]
        matrix = []
        for k in selectedIndices[i][j]:
            matrix.append(rawMatrix[k])

        m_AttValues = []

        for k in range(len(matrix)):
            
            array = vars(matrix[k])['m_AttValues']
            if useFxp:
                array = [toFxp(_i) for _i in array]
            m_AttValues += array
            
        decls += "\nconst " + ("FixedNum" if useFxp else "float") + " tmp1_AttValues" + str(i) + "_" + str(j) + "[" + str(len(m_AttValues)) + "] = " + str(m_AttValues).replace(']','}').replace('[','{').replace('\'','') + ";\n"
        inits += "\ttmp0_AttValues" + str(i) + "[" + str(j) + "] = tmp1_AttValues" + str(i) + "_" + str(j) + ";\n"
    inits += "\tm_AttValues[" + str(i) + "] = tmp0_AttValues" + str(i) + ";\n\n"

#vars(binarySMO)['m_b'] value
decls += "\nconst " + ("FixedNum" if useFxp else "float") + " *m_b[" + str(len(new_classifiers)) + "];\n"

for i in range(len(new_classifiers)):
    if len(new_classifiers[i]) == 0:
        inits += "\n\tm_b[" + str(i) + "] = NULL;\n"
        continue    
    m_b_i = []
    for j in range(len(new_classifiers[i])):
        m_b_i.append(vars(new_classifiers[i][j])['m_b'])
    if useFxp:
        m_b_i = [toFxp(_i) for _i in m_b_i]
    decls += "const " + ("FixedNum" if useFxp else "float") + " tmp_m_b" + str(i) + "[" + str(len(m_b_i)) + "] = " + str(m_b_i).replace(']','}').replace('[','{').replace('\'','') + ";\n"
    inits += "\tm_b[" + str(i) + "] = tmp_m_b" + str(i) + ";\n"

inits += "}\n"

################################ INITIALIZATIONS ################################

################################ DEFINES ################################

defs += "#define INPUT_SIZE " + str(len(inputs)) + "\n"
defs += "#define NUM_CLASSES " + str(m_numClasses) + "\n"
#defs += "#define NAN nanf(\"\")\n"
defs += "#define CLASS_INDEX " + str(m_classIndex) + "\n"
defs += "#define M_GAMMA " + (toFxp(m_gamma) if useFxp else str(m_gamma)) + "\n"
#defs += "#define NAN 414141.41\n"
#defs += "#define SELECTED_ATT_SIZE " + str(len(m_SelectedAttributes)-1) + "\n"
#defs += "#define NUM_PREDICTORS " + str(m_NumPredictors) + "\n"
#defs += "#define INF 100000\n"
#defs += "#define isInf(x) ((x) == ((1.0)/(0.0)))\n"

################################ INCLUDES ################################

incls += "#include <Arduino.h>\n"\
         + (("#define TOTAL_BITS " + str(totalBits) +\
             "\n#define FIXED_FBITS " + str(fixedBits) +\
             "\n#define SIGNED" +\
             "\n#include \"FixedNum.h\"\n") if useFxp else "")

file.write(incls)
file.write(defs)
file.write(decls)
file.write(funcs)
file.write(inits)

file.close()
