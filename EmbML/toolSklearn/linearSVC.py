
import pickle
import numpy as np
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

try: modelFile = open(sys.argv[1], "r")
except:
    print "Error: model file invalid"
    exit()

obj = pickle.load(modelFile)

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

def predict(x):
    scores = [sum(x * clf.coef_[i]) + clf.intercept_[i] for i in range(len(clf.coef_))]
    return np.argmax(scores)

coef = obj.coef_.tolist()
intercept = obj.intercept_.tolist()
classes = list(map(int, obj.classes_.tolist()))

#######################################################################################################
# Write the classifier file

funcs = "\n"
decls = "\n"
inits = "\n"
defs = "\n"
incls = "\n"

################################ FUNCTIONS ################################

### classify function
#funcs += "\n/* Function classify description:\n\
# * Instance array must be initializated, with appropriated attributes, before calling this function\n"

#for i in range(len(classes)):
#    funcs += " * Output number " +\
#             str(i) +\
#             " means that the instance was classified as " +\
#             classes[i] +\
#             "\n"   
#funcs += " */\n"

funcs += "int classify(){\n\
\tint indMax = 0;\n\
\t" + ("FixedNum" if useFxp else "float") + " scores[NUM_CLASSES];\n\
\tfor (int i = 0; i < NUM_CLASSES; i++){\n\
\t\tscores[i] = intercept[i];\n\
\t\tfor (int j = 0; j < INPUT_SIZE; j++){\n\
\t\t\tscores[i] " +\
("= fxp_sum(scores[i], fxp_mul(coef[i][j], instance[j]))" if useFxp\
 else "+= (coef[i][j] * instance[j])") + ";\n\
\t\t}\n\
\t\tif (scores[i] " + ("<" if len(classes) == 2 else ">") + " scores[indMax]){\n\
\t\t\tindMax = i;\n\
\t\t}\n\
\t}\n\
\treturn classes[indMax];\n\
}\n"

################################ DECLARATIONS ################################

### print sorted attributes
#decls += "/* Instance array must be global\n \
#* Attributes MUST be sorted in instance array in the following order:\n"
#for i in attributes:
#    decls += " * " +\
#             i +\
#             "\n"

### instance array
#decls += " */\n"
decls += ("FixedNum" if useFxp else "float") +\
         " instance[INPUT_SIZE+1];\n"

### coef array
decls += "\nconst " + ("FixedNum" if useFxp else "float") + \
         " coef[NUM_CLASSES][INPUT_SIZE] = " +\
         str([[toFxp(coef[_i][_j]) for _j in range(len(coef[_i]))]\
              for _i in range(len(coef))]\
        if useFxp\
        else \
             coef).replace(']','}').replace('[','{').replace('\'','') +\
         ";\n"

### intercept array
decls += "\nconst " +\
        ("FixedNum" if useFxp else "float") +\
        " intercept[NUM_CLASSES] = {" +\
        str([toFxp(_i)\
             for _i in intercept]\
        if useFxp\
        else \
            intercept).replace(']','').replace('[','').replace('\'','') +\
        "};\n"

### classes array
decls += "\nconst " + chooseDataType(classes) +\
         " classes[NUM_CLASSES] = " +\
         str(classes).replace(']','}').replace('[','{') + ";\n"

################################ DEFINES ################################

defs += "#define NUM_CLASSES " + str(len(classes)) + "\n"
defs += "#define INPUT_SIZE " + str(len(coef[0])) + "\n"

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
