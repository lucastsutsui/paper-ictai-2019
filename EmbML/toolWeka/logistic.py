
import javaobj
import math
import sys

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

#######################################################################################################

m_Par = vars(obj)['m_Par']
m_NumPredictors = vars(obj)['m_NumPredictors']
m_ClassIndex = vars(obj)['m_ClassIndex']
m_NumClasses = vars(obj)['m_NumClasses']
m_SelectedAttributes = vars(vars(vars(obj)['m_AttFilter'])['m_removeFilter'])['m_SelectedAttributes']

#######################################################################################################
# Recover class names
try:
    classesNames = vars(vars(vars(vars(vars(vars(vars(vars(obj)\
                    ['m_AttFilter'])['m_OutputRelAtts'])['m_Data'])\
                    ['m_Attributes'])['annotations'][m_ClassIndex+1])\
                    ['m_AttributeInfo'])['m_Hashtable'])['annotations'][1:]
except:
    try:
        classesNames = vars(vars(vars(vars(vars(vars(obj)\
                        ['m_structure'])['m_Attributes'])\
                        ['annotations'][m_ClassIndex+1])\
                        ['m_AttributeInfo'])['m_Hashtable'])\
                        ['annotations'][1:]
    except:
        print "Error: can't recover class names"
        exit()
        
outputs = []
className = ''
for i in classesNames:
    if type(i) == str or 'String' in str(type(i)):
        className = i
    else:
        outputs.append((vars(i)['value'],className))
outputs.sort()

#######################################################################################################
# Recover attribute names
try:
    attributesNames = vars(vars(vars(vars(vars(vars(obj)\
                        ['m_AttFilter'])['m_removeFilter'])\
                        ['m_InputRelAtts'])['m_Data'])\
                        ['m_Attributes'])['annotations'][1:]
    m_oldClassIndex = vars(vars(vars(vars(vars(obj)\
                        ['m_AttFilter'])['m_removeFilter'])\
                        ['m_InputRelAtts'])['m_Data'])\
                        ['m_ClassIndex']
except:
    print "Error: can't recover attribute names"
    exit()
    
inputs = []
attName = ''
for i in attributesNames:
    inputs.append((vars(i)['m_Index'], vars(i)['m_Name']))
inputs.sort()

#######################################################################################################

funcs = "\n"
decls = "\n"
inits = "\n"
defs = "\n"
incls = "\n"

################################ FUNCTIONS ################################

### classify function
funcs += "/* Function classify description:\n\
 * Instance array must be initializated, with \
appropriated attributes, before calling this function\n"

for i,j in outputs:
    funcs += " * Output number " + str(i) + \
             " means that the instance was classified as "\
             + j + "\n"
    
funcs += " */\n"
funcs += "int classify(){\n\
\t" + ("FixedNum" if useFxp else "float") + " prob[NUM_CLASSES];\n\
\t" + ("FixedNum" if useFxp else "float") + " newInstance[NUM_PREDICTORS+1];\n\
\tnewInstance[0] = " + (toFxp(1.0) if useFxp else "1.0") + ";\n\
\tfor (int i = 1; i <= SELECTED_ATT_SIZE; i++){\n\
\t\tif (m_SelectedAttributes[i] <= CLASS_INDEX) {\n\
\t\t\tnewInstance[i] = instance[m_SelectedAttributes[i-1]];\n\
\t\t}\n\
\t\telse {\n\
\t\t\tnewInstance[i] = instance[m_SelectedAttributes[i]];\n\
\t\t}\n\
\t}\n\
\t" + ("FixedNum" if useFxp else "float") + " v[NUM_CLASSES] = {0};\n\
\tfor (int i = 0; i < NUM_CLASSES-1; i++) {\n\
\t\tfor (int j = 0; j <= NUM_PREDICTORS; j++) {\n\
\t\t\t" + ("v[i] = fxp_sum(v[i], fxp_mul(m_Par[(i * (NUM_PREDICTORS + 1)) + j], newInstance[j]))"\
           if useFxp else\
           "v[i] += m_Par[(i * (NUM_PREDICTORS + 1)) + j] * newInstance[j]") + ";\n\
\t\t}\n\
\t}\n\
\tv[NUM_CLASSES-1] = 0;\n\
\tfor (int i = 0; i < NUM_CLASSES; i++) {\n\
\t\t" + ("FixedNum" if useFxp else "float") + " acc = " +\
("0" if useFxp else "0.0") + ";\n\
\t\tfor (int j = 0; j < NUM_CLASSES-1; j++) {\n\
\t\t\t" + ("acc = fxp_sum(acc, fxp_exp(fxp_diff(v[j], v[i])))"\
           if useFxp else "acc += exp(v[j]-v[i])") + ";\n\
\t\t}\n\
\t\tprob[i] = " + (("fxp_div(" + toFxp(1.0) + ", fxp_sum(acc, fxp_exp(-v[i])))")\
                   if useFxp else "1.0 / (acc + exp(-v[i]))") + ";\n\
\t}\n\
\tint indexMax = 0;\n\
\tfor (int i = 1; i < NUM_CLASSES; i++) {\n\
\t\tif (prob[i] > prob[indexMax]) {\n\
\t\t\tindexMax = i;\n\
\t\t}\n\
\t}\n\
\treturn indexMax;\n\
}"

################################ DECLARATIONS ################################

### print sorted attributes
decls += "/* Instance array must be global\n\
 * Attributes MUST be sorted in instance array in the following order:\n"

for i,j in inputs:
    if i != m_oldClassIndex:
        decls += " * " + j + "\n"
decls += " */\n" + ("FixedNum" if useFxp else "float") + " instance[INPUT_SIZE+1];\n"

if useFxp:
    m_Par = [[toFxp(_j) for _j in _i] for _i in m_Par]

new_Par = []
for i in range(m_NumClasses - 1):
    for j in range(m_NumPredictors + 1):
        new_Par.append(m_Par[j][i])

### print m_Par array
decls += "const " + ("FixedNum" if useFxp else "float") +\
         " m_Par[" + str(len(new_Par)) + "] = " +\
         str(new_Par).replace('[','{').replace(']','}').replace('\'','') +\
         ";\n"

### print m_NotSelectedAttributes array
decls += "const int m_SelectedAttributes[" + str(len(m_SelectedAttributes)) +\
         "] = " + str(m_SelectedAttributes).replace('[','{').replace(']','}') +\
         ";\n"

################################ DEFINES ################################

defs += "#define INPUT_SIZE " + str(len(inputs)-1) + "\n"
defs += "#define NUM_CLASSES " + str(m_NumClasses) + "\n"
defs += "#define SELECTED_ATT_SIZE " + str(len(m_SelectedAttributes)-1) + "\n"
defs += "#define NUM_PREDICTORS " + str(m_NumPredictors) + "\n"
defs += "#define CLASS_INDEX " + str(m_ClassIndex) + "\n"

################################ INCLUDES ################################

incls += "#include <Arduino.h>\n" + (\
            ("\n#define TOTAL_BITS " + str(totalBits) +\
             "\n#define FIXED_FBITS " + str(fixedBits) +\
             "\n#define SIGNED" +\
             "\n#define OVERFLOW_DETECT" +\
             "\n#include \"FixedNum.h\"\n") if useFxp else "#include <math.h>\n")

file.write(incls)
file.write(defs)
file.write(decls)
file.write(funcs)
file.write(inits)

file.close()
