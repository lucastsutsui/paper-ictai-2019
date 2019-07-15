
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

m_useLaplace = vars(obj)['m_useLaplace']

# Recover index for class attribute
try:
    m_classIndex = vars(vars(vars(obj)['m_root'])['m_train'])['m_ClassIndex']
except:
    print "Error: can't recover class index"
    exit(0)

#######################################################################################################
# Recover attribute names
attributes = []
try:
    inputs = vars(vars(vars(vars(obj)['m_root'])['m_train'])['m_NamesToAttributeIndices'])['annotations'][1:]
    attributes = ['' for _ in range((len(inputs)/2) - 1)]
    for i in range(len(inputs)):
        if i % 2 == 0 or inputs[i-1] == 'class' or inputs[i-1] == 'label':
            continue
        index = vars(inputs[i])['value']
        attributes[index - (1 if index > m_classIndex else 0)] = inputs[i-1]
except:
    print "Error: can't recover attribute names"
    print "Make sure class atribute is named \'class\' or \'label\' in training dataset."
    exit(0)

#######################################################################################################
# Recover class names
classes = []
try:
    outputs = vars(vars(vars(vars(vars(vars(vars(obj)['m_root'])['m_train'])['m_Attributes'])['annotations'][1:][m_classIndex])['m_AttributeInfo'])['m_Hashtable'])['annotations'][1:]
    classes = ['' for _ in range(len(outputs)/2)]
    for i in range(len(outputs)):
        if i % 2 == 0:
            continue
        classes[vars(outputs[i])['value']] = outputs[i-1]
except:
    print "Error: can't recover class names"
    exit(0)

#######################################################################################################
m_numClasses = len(classes)

tree = []
m_isLeaf = []
m_attIndex = []
m_splitPoint = []
m_totaL = []
m_perClass = []
m_perBag = []
m_perClassPerBag = []

# Returns length of the tree
def dfsLenTree(obj):
    if vars(obj)['m_isLeaf']:
        return 1
    return sum([dfsLenTree(_i) for _i in vars(obj)['m_sons']]) + 1

# Recovers the structure of the tree
def dfs(obj, index):
    i = index
    
    if vars(obj)['m_isLeaf']:
        m_isLeaf[i] = True
        #return i
        
    m_perClass[i] = vars(vars(vars(obj)['m_localModel'])['m_distribution'])['m_perClass']
    m_perBag[i] = vars(vars(vars(obj)['m_localModel'])['m_distribution'])['m_perBag']
    m_perClassPerBag[i] = vars(vars(vars(obj)['m_localModel'])['m_distribution'])['m_perClassPerBag']
    m_isEmpty[i] = vars(obj)['m_isEmpty']
    m_totaL[i] = vars(vars(vars(obj)['m_localModel'])['m_distribution'])['totaL']
    
    if 'm_attIndex' in vars(vars(obj)['m_localModel']):
        m_attIndex[i] = vars(vars(obj)['m_localModel'])['m_attIndex']
    if 'm_splitPoint' in vars(vars(obj)['m_localModel']):
        m_splitPoint[i] = vars(vars(obj)['m_localModel'])['m_splitPoint']
    if type(vars(obj)['m_sons']) != type(None):
        for _i in vars(obj)['m_sons']:
            i,childIndex = dfs(_i, i+1)
            tree[index].append(childIndex)
        
    return (i,index)
    
lenTree = dfsLenTree(vars(obj)['m_root'])

tree = [[] for _ in range(lenTree)]
m_isLeaf = [False for _ in range(lenTree)]
m_attIndex = [-1 for _ in range(lenTree)]
m_splitPoint = [-1 for _ in range(lenTree)]
m_isEmpty = [False for _ in range(lenTree)]
m_totaL = [0 for _ in range(lenTree)]
m_perClass = [[] for _ in range(lenTree)]
m_perBag = [[] for _ in range(lenTree)]
m_perClassPerBag = [[] for _ in range(lenTree)]

dfs(vars(obj)['m_root'], 0)

# Save the indexes for empty nodes
emptyIndex = [i for i in range(len(m_isEmpty)) if m_isEmpty[i]]

for i in range(len(m_attIndex)):
    if m_isEmpty[i]:
        m_attIndex[i] = -2

attOffset = len(attributes) + 2

def getProb1(i):
    probPerClass = []
    if m_useLaplace:
        probPerClass = [((m_perClass[i][j] + 1.0) / float(m_totaL[i] + m_numClasses))\
                        for j in range(len(m_perClass[i]))]
    else:
        if m_totaL[i] != 0:
            probPerClass = [(m_perClass[i][j] / float(m_totaL[i]))\
                            for j in range(len(m_perClass[i]))]
        else:
            probPerClass = [0.0 for j in range(len(m_perClass[i]))]
    return probPerClass.index(max(probPerClass)) + attOffset

def getProb2(i, j):
    probPerClass = []
    if m_perBag[i][j] > 0:
        if m_useLaplace:
            probPerClass = [((m_perClassPerBag[i][j][k] + 1.0) /\
                            float(m_perBag[i][j] + m_numClasses))\
                            for k in range(len(m_perClassPerBag[i][j]))]
        else:
            probPerClass = [(m_perClassPerBag[i][j][k] /\
                            float(m_perBag[i][j]))\
                            for k in range(len(m_perClassPerBag[i][j]))]
    else:
        return getProb1(i)
    return probPerClass.index(max(probPerClass)) + attOffset
    
def setPrediction(i):
    if m_isLeaf[i]:
        # leaf
        m_attIndex[i] = getProb1(i)
    else:
        for j in range(len(tree[i])):
            if m_isEmpty[i]:
                # empty son
                m_attIndex[i] = getProb2(i, j)
            else:
                setPrediction(tree[i][j])


setPrediction(0)

#######################################################################################################
# Write the classifier file

funcs = "\n"
decls = "\n"
inits = "\n"
defs = "\n"
incls = "\n"

################################ FUNCTIONS ################################

### classify function
funcs += "\n/* Function classify description:\n\
 * Instance array must be initializated, with appropriated attributes, before calling this function\n"

for i in range(len(classes)):
    funcs += " * Output number " +\
             str(i) +\
             " means that the instance was classified as " +\
             classes[i] +\
             "\n"
    
funcs += " */\n"
funcs += "int classify(){\n\
\tint i = M_ROOT;\n\
\twhile (i != -1 && m_attIndex[i] < ATT_OFFSET){\n\
\t\ti = tree[i][(instance[m_attIndex[i]] <= m_splitPoint[i] ? 0 : 1)];\n\
\t}\n\
\treturn (m_attIndex[i] - ATT_OFFSET);\n\
}\n"

################################ DECLARATIONS ################################

### print sorted attributes
decls += "/* Instance array must be global\n \
* Attributes MUST be sorted in instance array in the following order:\n"
for i in attributes:
    decls += " * " +\
             i +\
             "\n"

### instance array
decls += " */\n" +\
         ("FixedNum" if useFxp else "float") +\
         " instance[INPUT_SIZE+1];\n"

### m_attIndex array
decls += "\nconst " + chooseDataType(m_attIndex) + " m_attIndex[LEN_TREE] = {" +\
         str(m_attIndex).replace(']','').replace('[','') +\
         "};\n"

### m_splitPoint array
decls += "\nconst " +\
        ("FixedNum" if useFxp else "float") +\
        " m_splitPoint[LEN_TREE] = {" +\
        str([toFxp(_i)\
        for _i in m_splitPoint]\
        if useFxp\
        else \
        m_splitPoint).replace(']','').replace('[','').replace('\'','') +\
        "};\n"

for i in range(len(tree)):
    if len(tree[i]) == 0:
        tree[i] = [-1, -1]
        
arrayTree = []
for i in tree:
    arrayTree += i
    
decls += "\nconst " + chooseDataType(arrayTree) + " tree[LEN_TREE][2] = " + str(tree).replace(']','}').replace('[','{') + ";\n"

################################ DEFINES ################################

defs += "#define M_ROOT 0\n"
defs += "#define NUM_CLASSES " + str(m_numClasses) + "\n"
defs += "#define CLASS_INDEX " + str(m_classIndex) + "\n"
defs += "#define LEN_TREE " + str(lenTree) + "\n"
defs += "#define INPUT_SIZE " + str(len(attributes)) + "\n"
defs += "#define ATT_OFFSET " + str(attOffset) + "\n"

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
