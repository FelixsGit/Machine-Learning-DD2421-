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

print("linear_kernel test", linear_kernel((2, 3), (1, 1)))
print("poly_kernel test", poly_kernel((2, 3), (1, 1), 2))
print("rbf_kernel test", radial_basis_function_kernel((2, 3), (1, 1), 1))

#################ASSIGMENT 2###########################################

matrix = numpy.zeros(shape=(5, 5))
def calculate_matrix(x_vector, t_vector):
    for i in range(0, len(x_vector)):
        for j in range(0, len(x_vector)):
            matrix[i][j] = t_vector[i] * t_vector[j] * linear_kernel(x_vector[i], x_vector[j])


calculate_matrix(((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), (1, -1, 1, -1, 1))
print(matrix)

def objective(vector):
    vector_sum = numpy.sum(vector)
    scalar = 0
    for i in range(0, len(vector)):
        for j in range(0, len(vector)):
            scalar = scalar + vector[i] * vector[j] * matrix[i][j]

    scalar = (scalar/2) - vector_sum
    return scalar

print(objective((1, 2, 3, 4, 5)))

##################ASSIGMENT 3################################

def zero_fun(vector, t_vector):
    return numpy.absolute(numpy.dot(vector, t_vector))

print(zero_fun(((1, 1), (2, 2)), (-1, -1)))

##################ASSIGMENT 4################################


x_vector = [(1, 1), (2, 2)]
t_vector = [1, -1]
start = numpy.zeros(10)
ret = minimize(objective, start, bounds=B, constraints=XC)
alpha = ret['x']
if(ret['success']):
    for i in range (0, len(alpha)):
        if((alpha <= 0.000001) | (alpha >= -0.000001)):
            list.append((alpha, x_vector[i], t_vector[i]))

