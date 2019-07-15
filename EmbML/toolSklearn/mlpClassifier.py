
import pickle
import numpy as np
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

hidden_layer_sizes = obj.hidden_layer_sizes
if not hasattr(hidden_layer_sizes, "__iter__"):
    hidden_layer_sizes = [hidden_layer_sizes]
hidden_layer_sizes = list(hidden_layer_sizes)

n_layers = obj.n_layers_
coefs = [_i.tolist() for _i in obj.coefs_]
intercepts = [_i.tolist() for _i in obj.intercepts_]
input_size = len(coefs[0])
output_size = obj.n_outputs_
end = [input_size] + hidden_layer_sizes + [output_size]
for i in range(1, len(end)): end[i] += end[i-1]
number_neurons = end[-1]
classes = map(int, obj.classes_.tolist())

activation_hidden = obj.activation
activation_output = obj.out_activation_

for i in range(len(coefs)):
    for j in range(len(coefs[i])):
        for k in range(len(coefs[i][j])):
            if abs(coefs[i][j][k]) < 1e-9:
                coefs[i][j][k] = 0.0

class_threshold = -1.0
if len(classes) == 2:
    class_threshold = (obj._label_binarizer.pos_label + obj._label_binarizer.neg_label) / 2.0
    

#######################################################################################################
# Write the classifier file

funcs = "\n"
decls = "\n"
inits = "\n"
defs = "\n"
incls = "\n"

inits += "void initConnections(){"

################################ FUNCTIONS ################################

# Activation Functions
#"fxp_div(fxp_exp(fxp_diff(x, max_elem)), sum_elem)"
softmax_function = "\treturn " +\
                    ("fxp_diff(x, max_elem)"\
                     if useFxp else\
                     "(x - max_elem)") +\
                    ";\n}\n"

logistic_function = "\treturn " +\
                     (("fxp_div(" + toFxp(1) +\
                      ", fxp_sum(" + toFxp(1) +\
                      ", fxp_exp(-x)))")\
                      if useFxp else\
                      "1.0 / (1.0 + exp(-x))") +\
                     ";\n}\n"

relu_function = "\treturn " +\
                 (("max(" + toFxp(0) + ", x)")\
                  if useFxp else\
                  "max(0.0, x)") +\
                 ";\n}\n"

# Select activation function for hidden layer neurons
funcs += ("FixedNum" if useFxp else "float") +\
         " activation_hidden(" +\
         ("FixedNum" if useFxp else "float") +\
         " x){\n"
if activation_hidden == 'logistic': funcs += logistic_function
elif activation_hidden == 'relu': funcs += relu_function
else:
    print "Activation function " + activation_hidden + " not supported!"
    exit()

# Select activation function for output layer neurons
funcs += ("FixedNum" if useFxp else "float") +\
         " activation_output(" +\
         ("FixedNum" if useFxp else "float") +\
         " x, " +\
         ("FixedNum" if useFxp else "float") +\
         " max_elem){\n"
if activation_output == 'logistic': funcs += logistic_function
elif activation_output == 'relu': funcs += relu_function
elif activation_output == 'softmax': funcs += softmax_function
else:
    print "Activation function " + activation_output + " not supported!"
    exit()

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
\t" + ("FixedNum" if useFxp else "float") + " values[N_NEURONS];\n\
\t" + ("FixedNum" if useFxp else "float") + " max_output;\n\
\tfor (int i = 0; i < INPUT_SIZE; i++){\n\
\t\tvalues[i] = instance[i];\n\
\t}\n\
\tfor (int i = 0; i < N_LAYERS - 1; i++){\n\
\t\tfor (int j = end[i]; j < end[i + 1]; j++){\n\
\t\t\tvalues[j] = " + (toFxp(0) if useFxp else "0.0") + ";\n\
\t\t\tint offset = ((i == 0) ? (0) : (end[i - 1]));\n\
\t\t\tfor (int k = 0; k < (end[i] - offset); k++){\n\
\t\t\t\tvalues[j] " +\
("= fxp_sum(fxp_mul(coefs[i][(k * (end[i + 1] - end[i])) + (j - end[i])], values[offset + k]), values[j])"\
 if useFxp else\
 "+= (coefs[i][(k * (end[i + 1] - end[i])) + (j - end[i])] * values[offset + k])") +\
 ";\n\
\t\t\t}\n\
\t\t\tvalues[j] " +\
("= fxp_sum(intercepts[i][j - end[i]], values[j])"\
 if useFxp else\
 "+= intercepts[i][j - end[i]]") +\
";\n\
\t\t\tif ((i + 1) != (N_LAYERS - 1)){\n\
\t\t\t\tvalues[j] = activation_hidden(values[j]);\n\
\t\t\t}\n\
\t\t\telse if (j == end[i]){\n\
\t\t\t\tmax_output = values[j];\n\
\t\t\t}\n\
\t\t\telse{\n\
\t\t\t\tmax_output = max(max_output, values[j]);\n\
\t\t\t}\n\
\t\t}\n\
\t}\n"
if len(classes) == 2:
    funcs += "\treturn classes[(activation_output(values[end[N_LAYERS - 2]], max_output) > CLASS_THRESHOLD)];\n\
}\n"
else:
    funcs += "\tint indMax = end[N_LAYERS - 2];\n\
\tfor (int i = end[N_LAYERS - 2]; i < end[N_LAYERS - 1]; i++){\n\
\t\tvalues[i] = activation_output(values[i], max_output);\n\
\t\tif (values[i] > values[indMax]) indMax = i;\n\
\t}\n\
\treturn classes[indMax - end[N_LAYERS - 2]];\n\
}\n"

################################ DECLARATIONS ################################

### print sorted attributes
#decls += "/* Instance array must be global\n \
#* Attributes MUST be sorted in instance array in the following order:\n"
#for i in attributes:
#    decls += " * " +\
#             i +\
#             "\n"

### instance array OK
#decls += " */\n"
decls += ("FixedNum" if useFxp else "float") +\
         " instance[INPUT_SIZE+1];\n"

### end array OK
decls += "\nconst " + chooseDataType(end) +\
         " end[N_LAYERS] = " +\
         str(end).replace(']','}').replace('[','{') +\
         ";\n"

### coefs array OK
decls += "\nconst " +\
        ("FixedNum" if useFxp else "float") +\
        " *coefs[N_LAYERS - 1];\n"
for i in range(len(coefs)):
    if len(coefs[i]) == 0:
        inits += "\n\coefs[" + str(i) + "] = NULL;"
        continue

    array = coefs[i]
    decls += "\nconst " + ("FixedNum" if useFxp else "float") + \
         " coefs_" + str(i) + "[" + str(len(array)) + " * " +\
         str(len(array[0])) + "] = {" + \
         str([[toFxp(array[_i][_j]) for _j in range(len(array[0]))]\
              for _i in range(len(array))]\
             if useFxp else \
             array).replace(']','').replace('[','').replace('\'','') +\
         "};\n"
    inits += "\n\tcoefs[" + str(i) + "] = coefs_" + str(i) + ";"

### intercepts array OK
decls += "\nconst " +\
        ("FixedNum" if useFxp else "float") +\
        " *intercepts[N_LAYERS - 1];\n"
for i in range(len(intercepts)):
    if len(intercepts[i]) == 0:
        inits += "\n\tintercepts[" + str(i) + "] = NULL;"
        continue

    array = intercepts[i]
    decls += "\nconst " + ("FixedNum" if useFxp else "float") + \
         " intercepts_" + str(i) + "[" + str(len(array)) + "] = " + \
         str([toFxp(array[_j]) for _j in range(len(array))]\
             if useFxp else\
             array).replace(']','}').replace('[','{').replace('\'','') +\
         ";\n"
    inits += "\n\tintercepts[" + str(i) + "] = intercepts_" + str(i) + ";"

### classes array OK
decls += "\nconst " + chooseDataType(classes) +\
         " classes[NUM_CLASSES] = " +\
         str(classes).replace(']','}').replace('[','{') + ";\n"

inits += "\n}\n"

################################ DEFINES ################################

defs += "#define NUM_CLASSES " + str(len(classes)) + "\n"
if len(classes) == 2:
    defs += "#define CLASS_THRESHOLD " + (toFxp(class_threshold)\
                                         if useFxp else\
                                         str(class_threshold)) + "\n"
defs += "#define INPUT_SIZE " + str(input_size) + "\n"
defs += "#define N_LAYERS " + str(n_layers) + "\n"
defs += "#define N_NEURONS " + str(end[-1]) + "\n"

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
