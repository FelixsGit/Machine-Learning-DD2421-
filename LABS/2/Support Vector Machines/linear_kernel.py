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

classA = numpy.concatenate((numpy.random.randn(10,2)*0.2+[1.5,0.5], numpy.random.randn(10,2)*0.2+[-1.5,1.5]))
classB = numpy.random.randn(20, 2)*0.2+[0.0, 1.0]

x_vector = numpy.concatenate((classA, classB))
t_vector = numpy.concatenate((numpy.ones(classA.shape[0]), -numpy.ones(classB.shape[0])))
N = x_vector.shape[0]

permute = list(range(N))
random.shuffle(permute)
x_vector = x_vector[permute, :]
t_vector = t_vector[permute]

C = 0.5

matrix = numpy.zeros(shape=(N, N))

def calculate_matrix(x_vector, t_vector):
    for i in range(0, len(x_vector)):
        for j in range(0, len(x_vector)):
            matrix[i][j] = t_vector[i] * t_vector[j] * linear_kernel(x_vector[i], x_vector[j])

calculate_matrix(x_vector, t_vector)
start = numpy.zeros(N)

def objective(alpha):
    vector_sum = numpy.sum(alpha)
    scalar = 0
    for i in range(0, len(alpha)):
        for j in range(0, len(alpha)):
            scalar = scalar + (alpha[i] * alpha[j] * matrix[i][j])
    scalar = (scalar/2) - vector_sum
    return scalar

##################ASSIGMENT 3################################

def zero_fun(vector):
    return numpy.dot(vector, t_vector)


##################ASSIGMENT 4################################
XC = {'type': 'eq', 'fun': zero_fun}
B = [(0, None) for b in range(N)]
ret = minimize(objective, start, bounds=B, constraints=XC)
print(ret)
alpha = ret['x']
support_vector_list = []
if ret['success']:
    for i in range(0, len(alpha)):
        if (alpha[i] >= 0.000001) or (alpha[i] <= -0.000001):
            support_vector_list.append([alpha[i], x_vector[i], t_vector[i]])
print("Support vector list:", support_vector_list)


##use all x_vector or only the 3 support vectors?
def calculate_b(sv_list):
    sum = 0
    for i in range(0, len(sv_list)):
        kern = linear_kernel(sv_list[0][1], sv_list[i][1])
        alpha_target = sv_list[i][0] * sv_list[i][2]
        sum += (alpha_target * kern)
    sum = sum - sv_list[0][2]
    return sum

b = calculate_b(support_vector_list)
print("b =", b)


def indicator_function(sv_list, new_point, b):
    sum = 0
    for i in range(0, len(sv_list)):
        kern = linear_kernel(new_point, sv_list[i][1])
        alpha_target = sv_list[i][0] * sv_list[i][2]
        sum += (alpha_target * kern)
    sum = sum - b
    return sum

result = indicator_function(support_vector_list, (1,1), b)
print("result ", result)



#############PLOTTING THE DECISION BOUNDARY & MARGIN LINES#####################
xgrid = numpy.linspace(-5, 5)
ygrid = numpy.linspace(-4, 4)
grid = numpy.array([[indicator_function(support_vector_list, (x, y), b) for x in xgrid] for y in ygrid])

plt.plot([p[0] for p in classA], [p[1] for p in classA], 'b.')
plt.plot([p[0] for p in classB], [p[1] for p in classB], 'r.')
for i in range(len(support_vector_list)):
    plt.plot([support_vector_list[i][1][0]], [support_vector_list[i][1][1]], 'y+')

plt.contour(xgrid, ygrid, grid, (-1.0, 0.0, 1.0), colors=('red', 'yellow', 'blue'), linewidths=(0.5, 0.5, 0.5))

plt.axis('equal')
plt.show()
