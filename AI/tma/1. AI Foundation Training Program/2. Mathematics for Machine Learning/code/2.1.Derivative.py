
import sympy as sp

def derivative_sympy(func, var, x_value):
    diff = sp.diff(func, var)
    return diff.subs(var, x_value)


def derivative_numerical(func, x, h=1e-5):
    return (func(x + h) - func(x)) /h


def derivative_numerical_sympy(func, var, x_value, h=1e-5):
    func_lambda = sp.lambdify(var, func, 'numpy')
    return (func_lambda(x_value + h) - func_lambda(x_value)) /h


# Ví dụ sử dụng
def func(x):
    return x**2 + 3*x + 2

x_value = 5.0
derivative_value = derivative_numerical(func, x_value)
print(f"Đạo hàm của hàm tại x = {x_value} sử dụng phương pháp số học là: {derivative_value}")


# Ví dụ sử dụng
x = sp.symbols('x')
func = x**2 + 3*x + 2
derivative = derivative_sympy(func, x, x_value)
print(f"Đạo hàm của hàm tại x = {x_value} sử dụng SymPy là:", derivative)

derivative_value = derivative_numerical_sympy(func, x, x_value)
print(f"Đạo hàm của hàm tại x = {x_value} sử dụng phương pháp số học là: {derivative_value}")
