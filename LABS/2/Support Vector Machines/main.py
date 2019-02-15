import numpy, random, math
from scipy . optimize import minimize
import matplotlib . pyplot as plt

#################ASSIGMENT 1####################################
def linear_kernel(x, y):
    return numpy.dot(x, y)

def poly_kernel(x, y, p):
    return math.pow((numpy.dot(x, y) + 1), p)

def radial_basis_function_kernel(x, y, smooth):
    x_minus_y = numpy.subtract(x, y)
    abs_x_minus_y = numpy.sqrt(x_minus_y.dot(x_minus_y))
    abs_x_minus_y_squared = math.pow(abs_x_minus_y, 2)
    final_exp = (abs_x_minus_y_squared/(2 * math.pow(smooth, 2))) * - 1
    return math.pow(math.e, final_exp)

#print("linear_kernel test", linear_kernel((2, 3), (1, 1)))
#print("poly_kernel test", poly_kernel((2, 3), (1, 1), 2))
#print("rbf_kernel test", radial_basis_function_kernel((2, 3), (1, 1), 1))

#################ASSIGMENT 2###########################################
t_vector = (-1, -1, 1, 1, 1)
x_vector = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
N = 5
matrix = numpy.zeros(shape=(N, N))

def calculate_matrix(x_vector, t_vector):
    for i in range(0, len(x_vector)):
        for j in range(0, len(x_vector)):
            matrix[i][j] = t_vector[i] * t_vector[j] * linear_kernel(x_vector[i], x_vector[j])

calculate_matrix(x_vector, t_vector)
start = numpy.zeros(N)
print(matrix)

def objective(alpha):
    vector_sum = numpy.sum(alpha)
    scalar = 0
    for i in range(0, len(alpha)):
        for j in range(0, len(alpha)):
            scalar = scalar + (alpha[i] * alpha[j] * matrix[i][j])
    #scalar = numpy.sum(numpy.dot(alpha, matrix))
    scalar = (scalar/2) - vector_sum
    return scalar

##################ASSIGMENT 3################################

def zero_fun(vector):
    return numpy.absolute(numpy.dot(vector, t_vector))



##################ASSIGMENT 4################################
XC = {'type': 'eq', 'fun': zero_fun}
B = [(0, None) for b in range(N)]
ret = minimize(objective, start, bounds=B, constraints=XC)
alpha = ret['x']
support_vector_list = []
print(ret)
if ret['success']:
    for i in range(0, len(alpha)):
        print("Examining alpha value =", alpha[i])
        if (alpha[i] >= 0.000001) & (alpha[i] <= -0.000001):
            support_vector_list.append([alpha, x_vector[i], t_vector[i]])
print("-----------> Support vector list:", support_vector_list)
