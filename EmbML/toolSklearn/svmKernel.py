
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

def maxMinArray(x):
    return [max(_i) for _i in x] + [min(_i) for _i in x]

#######################################################################################################

#LIBSVM_IMPL = ['c_svc', 'nu_svc', 'one_class', 'epsilon_svr', 'nu_svr']
#svm_type = LIBSVM_IMPL.index(obj._impl)
gamma = obj._gamma
coef0 = obj.coef0
degree = obj.degree
model_l = obj.support_.shape[0]
nr_class = obj.n_support_.shape[0]
n_class = nr_class * (nr_class - 1) / 2
input_size = obj.support_vectors_.shape[1]

dual_coef = obj._dual_coef_.tolist()
support_vectors = obj.support_vectors_.tolist()
n_support = obj.n_support_.tolist()
intercept = obj._intercept_.tolist()
classes = list(map(int, obj.classes_.tolist()))

# Remove zeros from dual_coef matrix
index_sv = []
end = []
lim = n_support
for i in range(1,nr_class): lim[i] += lim[i-1]

for i in range(len(dual_coef)):
    j = 0
    real_index = 0
    k = 0
    index_sv.append([])
    end.append([0])
    while real_index < model_l:
        if real_index >= lim[k]:
            end[i].append(j)
            k += 1
            
        if abs(dual_coef[i][j]) == 0.0:
            dual_coef[i].pop(j)
        else:
            index_sv[i].append(real_index)
            j += 1
        real_index += 1
    end[i].append(j)
        
#################################

# model->nr_class = clf.n_support_.shape[0]
# model->sv_coef = clf._dual_coef_
# model->l = clf.support_.shape[0]
# model->SV = clf.support_vectors_
# model->nSV = clf.n_support_
# model->rho = clf._intercept_

#def k_func_poly(x, y):
#    return math.pow((clf._gamma * sum(x*y) + clf.coef0), clf.degree)
#def k_func_rbf(x, y):
#    summ = 0.0
#    for i in range(len(x)):
#        summ += (x[i] - y[i]) * (x[i] - y[i])
#    return math.exp(-clf._gamma * summ)

#if svm_type > 1:
#    n_class = 1
#else:
#    n_class = clf.n_support_.shape[0]
#    n_class = n_class * (n_class - 1) // 2

#dec_values = np.empty((X.shape[0], n_class), dtype=np.float64)
#results = []

#for inst in range(X.shape[0]):
#    x = X[inst]
#
#    if svm_type >= 2:
#        summ = 0
#        for k in range(clf.support_.shape[0]):
#            summ += clf._dual_coef[0][k] * k_func_poly(x, clf.support_vectors_[k])
#        summ += clf._intercept_[0]
#        dec_values[0] = summ
#    else:
#        l = clf.support_.shape[0]
#        nr_class = clf.n_support_.shape[0]
#        
#        kvalue = [0.0 for k in range(l)]
#        for k in range(l): kvalue[k] = k_func_poly(x, clf.support_vectors_[k])
#        
#        start = [0 for k in range(nr_class)]
#        start[0] = 0
#        for k in range(1,nr_class): start[k] = start[k-1] + clf.n_support_[k-1]
#        
#        vote = [0 for k in range(nr_class)]
#    
#        p = 0
#        for i in range(nr_class):
#            for j in range(i+1,nr_class):
#                summ = 0
#                si = start[i]
#                sj = start[j]
#                ci = clf.n_support_[i]
#                cj = clf.n_support_[j]
#
#                for k in range(ci): summ += clf._dual_coef_[j-1][si+k] * kvalue[si+k]
#                for k in range(cj): summ += clf._dual_coef_[i][sj+k] * kvalue[sj+k]
#                
#                summ += clf._intercept_[p]
#                dec_values[inst][p] = summ
#                if dec_values[inst][p] > 0: vote[i] += 1
#                else: vote[j] += 1
#                p += 1
#                
#        vote_max_idx = 0
#        for i in range(1,nr_class):
#            if vote[i] > vote[vote_max_idx]:
#                vote_max_idx = i
#                
#        results.append(vote_max_idx)
#
#print sum(clf.predict(X) == clf.classes_.take(np.asarray(results, dtype=np.intp))), len(results)
#print sum(sum(dec_values == clf._dense_decision_function(X)))

#######################################################################################################
# Write the classifier file

funcs = "\n"
decls = "\n"
inits = "\n"
defs = "\n"
incls = "\n"

inits += "void initConnections(){"

################################ FUNCTIONS ################################

# Kernel Function
funcs  += ("FixedNum" if useFxp else "float") + \
          " k_function (const " + ("FixedNum" if useFxp else "float") + \
          " *y){\n"
if obj.kernel == 'linear':
    funcs += "\t" + ("FixedNum" if useFxp else "float") + " sum = " +\
             (toFxp(0) if useFxp else "0.0") + ";\n\
\tfor (int i = 0; i < INPUT_SIZE; i++){\n\
\t\tsum " + ("= fxp_sum(sum, fxp_mul(instance[i], y[i]))" if useFxp\
             else "+= instance[i] * y[i]") + ";\n\
\t}\n\
\treturn sum;\n\
}\n"
elif obj.kernel == 'rbf':
    funcs += "\t" + ("FixedNum" if useFxp else "float") + " sum = " +\
             (toFxp(0) if useFxp else "0.0") + ";\n\
\tfor (int i = 0; i < INPUT_SIZE; i++){\n\
\t\t" + ("FixedNum" if useFxp else "float") + " tmp = " + \
("fxp_diff(instance[i], y[i])" if useFxp else "instance[i] - y[i]") + ";\n\
\t\tsum += " + ("fxp_mul(tmp, tmp)" if useFxp else "tmp * tmp") + ";\n\
\t}\n\
\treturn " + ("fxp_exp(fxp_mul(-GAMMA, sum))" if useFxp\
              else "exp(-GAMMA * sum)") + ";\n\
}\n"
elif obj.kernel == 'poly':
    funcs += "\t" + ("FixedNum" if useFxp else "float") + " sum = " +\
             (toFxp(0) if useFxp else "0.0") + ";\n\
\tfor (int i = 0; i < INPUT_SIZE; i++){\n\
\t\tsum " + ("= fxp_sum(sum, fxp_mul(instance[i], y[i]))" if useFxp\
             else "+= instance[i] * y[i]") + ";\n\
\t}\n\
\treturn " + ("fxp_pow(fxp_sum(fxp_mul(GAMMA, sum), COEF0), DEGREE)" if useFxp\
              else "pow(GAMMA * sum + COEF0, DEGREE)") + ";\n\
}\n"
elif obj.kernel == 'sigmoid': # tanh needs to be implemented in fxp
    funcs += "\t" + ("FixedNum" if useFxp else "float") + " sum = " +\
             (toFxp(0) if useFxp else "0.0") + ";\n\
\tfor (int i = 0; i < INPUT_SIZE; i++){\n\
\t\tsum " + ("= fxp_sum(sum, fxp_mul(instance[i], y[i]))" if useFxp\
             else "+= instance[i] * y[i]") + ";\n\
\t}\n\
\treturn tanh(GAMMA * sum + COEF0);\n\
}\n"
else:
    print "Kernel " + obj.kernel + " not supported!"
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

funcs += "int classify(){\n"
#if svm_type >= 2:     # ONE_CLASS, EPSILON_SVR, and NU_SVR
#    funcs += "\t" + ("FixedNum" if useFxp else "float") + " sum = " +\
#             (toFxp(0) if useFxp else "0.0") + ";\n\
#\tfor (int i = 0; i < MODEL_L; i++){\n\
#\t\tsum += dual_coef[0][i] * k_function(support_vectors[i]);\n\
#\t}\n\
#\tsum += intercept[0];\n\
#\treturn sum;\n\
#}\n"
#else:
funcs += "\t" + ("FixedNum" if useFxp else "float") + " k_value[MODEL_L];\n\
\tfor (int i = 0; i < MODEL_L; i++){\n\
\t\tk_value[i] = k_function(support_vectors[i]);\n\
\t}\n\
\t" + chooseDataType(n_class) + " vote[NR_CLASS] = {0};\n\
\t" + chooseDataType(n_class) + " p = 0;\n\
\tfor (int i = 0; i < NR_CLASS - 1; i++){\n\
\t\tfor (int j = i + 1; j < NR_CLASS; j++){\n\
\t\t\t" + ("FixedNum" if useFxp else "float") + " sum = " +\
             (toFxp(0) if useFxp else "0.0") + ";\n\
\t\t\tfor (int k = end[j - 1][i]; k < end[j - 1][i + 1]; k++){\n\
\t\t\t\tsum " +\
("= fxp_sum(sum, fxp_mul(dual_coef[j - 1][k], k_value[index_sv[j - 1][k]]))"\
 if useFxp else\
 "+= dual_coef[j - 1][k] * k_value[index_sv[j - 1][k]]") + ";\n\
\t\t\t}\n\
\t\t\tfor (int k = end[i][j]; k < end[i][j + 1]; k++){\n\
\t\t\t\tsum " +\
("= fxp_sum(sum, fxp_mul(dual_coef[i][k], k_value[index_sv[i][k]]))"\
 if useFxp else\
 "+= dual_coef[i][k] * k_value[index_sv[i][k]]") + ";\n\
\t\t\t}\n\
\t\t\tsum " +\
("= fxp_sum(sum, intercept[p++])"\
 if useFxp else\
 "+= intercept[p++]") + ";\n\
\t\t\tif (sum > 0) vote[i]++;\n\
\t\t\telse vote[j]++;\n\
\t\t}\n\
\t}\n\
\tint indMax = 0;\n\
\tfor (int i = 1; i < NR_CLASS; i++){\n\
\t\tif (vote[i] > vote[indMax]) indMax = i;\n\
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

### instance array OK
#decls += " */\n"
decls += ("FixedNum" if useFxp else "float") +\
         " instance[INPUT_SIZE+1];\n"

### dual_coef array
decls += "\nconst " + ("FixedNum" if useFxp else "float") + \
         " *dual_coef[NR_CLASS - 1];\n"
for i in range(len(dual_coef)):
    if len(dual_coef[i]) == 0:
        inits += "\n\tdual_coef[" + str(i) + "] = NULL;"
        continue

    array = dual_coef[i]
    decls += "\nconst " + ("FixedNum" if useFxp else "float") + \
         " dual_coef_" + str(i) + "[" + str(len(array)) + "] = " + \
         str([toFxp(array[_j]) for _j in range(len(array))]\
        if useFxp\
        else \
             array).replace(']','}').replace('[','{').replace('\'','') +\
         ";\n"
    inits += "\n\tdual_coef[" + str(i) + "] = dual_coef_" + str(i) + ";"

### support_vectors array OK
decls += "\nconst " + ("FixedNum" if useFxp else "float") + \
         " support_vectors[MODEL_L][INPUT_SIZE] = " +\
         str([[toFxp(support_vectors[_i][_j]) for _j in range(len(support_vectors[i]))]\
              for _i in range(len(support_vectors))]\
        if useFxp\
        else \
             support_vectors).replace(']','}').replace('[','{').replace('\'','') +\
         ";\n"

### end array 
decls += "\nconst " + chooseDataType(maxMinArray(end)) +\
         " end[NR_CLASS - 1][NR_CLASS + 1] = " +\
         str(end).replace(']','}').replace('[','{') +\
         ";\n"

### index_sv array
index_sv_type = chooseDataType(maxMinArray(index_sv))
decls += "\nconst " + index_sv_type +\
         " *index_sv[NR_CLASS - 1];\n"
for i in range(len(index_sv)):
    if len(index_sv[i]) == 0:
        inits += "\n\tindex_sv[" + str(i) + "] = NULL;"
        continue

    array = index_sv[i]
    decls += "\nconst " + index_sv_type + \
         " index_sv_" + str(i) + "[" + str(len(array)) + "] = " + \
         str(array).replace(']','}').replace('[','{') +\
         ";\n"
    inits += "\n\tindex_sv[" + str(i) + "] = index_sv_" + str(i) + ";"

### intercept array OK
decls += "\nconst " +\
        ("FixedNum" if useFxp else "float") +\
        " intercept[N_CLASS] = {" +\
        str([toFxp(_i)\
             for _i in intercept]\
        if useFxp\
        else \
            intercept).replace(']','').replace('[','').replace('\'','') +\
        "};\n"

### classes array OK
decls += "\nconst " + chooseDataType(classes) +\
         " classes[NUM_CLASSES] = " +\
         str(classes).replace(']','}').replace('[','{') + ";\n"

inits += "\n}\n"

################################ DEFINES ################################

defs += "#define NUM_CLASSES " + str(len(classes)) + "\n"
defs += "#define INPUT_SIZE " + str(input_size) + "\n"
defs += "#define GAMMA " + (toFxp(gamma) if useFxp else str(gamma)) + "\n"
defs += "#define COEF0 " + (toFxp(coef0) if useFxp else str(coef0)) + "\n"
defs += "#define DEGREE " + (toFxp(degree) if useFxp else str(degree)) + "\n"
defs += "#define N_CLASS " + str(n_class) + "\n"
defs += "#define NR_CLASS " + str(nr_class) + "\n"
defs += "#define MODEL_L " + str(model_l) + "\n"

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
