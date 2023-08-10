# import cmath for complex number operations
import cmath
import numpy as np


def add():
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter the number: "))
    result = num1 + num2
    print("Addition = ", result)


def subtract():
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter the number: "))
    result = num1 - num2
    print("Subtraction = ", result)


def multiply():
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter the number: "))
    result = num1 * num2
    print("Multiplication = ", result)


def divide():
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter the number: "))
    result = num1 / num2
    print("Division = ", result)


def add_complex():
    num1 = complex(input("Enter the complex number (in the form a+bj): "))
    num2 = complex(input("Enter the complex number (in the form a+bj): "))
    result = num1 + num2
    print("Addition of Complex number = ", result)


def subtract_complex():
    num1 = complex(input("Enter the complex number (in the form a+bj): "))
    num2 = complex(input("Enter the complex number (in the form a+bj): "))
    result = num1 - num2
    print("Subtraction of Complex number = ", result)


def multiply_complex():
    num1 = complex(input("Enter the complex number (in the form a+bj): "))
    num2 = complex(input("Enter the complex number (in the form a+bj): "))
    result = num1 * num2
    print("Multiplication of Complex number = ", result)


def power():
    num = int(input("Enter the number: "))
    index = int(input("Enter the index: "))
    result = num ** index
    print("Power of given number = ", result)


def power_iota():
    power = int(input("Enter the power: "))
    # The cmath.exp() method accepts a complex number
    result = cmath.exp(1j * power * np.pi / 2)
    # and returns the exponential value.
    print("Result: ", result)


def add_matrices():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    matrix1 = []
    matrix2 = []

    print("Enter the elements of the first matrix:")
    for i in range(rows):
        row = []
        for j in range(columns):
            element = list(map(int, input().split()))
            row.append(element)
        matrix1.append(row)

    print("Enter the elements of the second matrix:")
    for i in range(rows):
        row = []
        for j in range(columns):
            element = list(map(int, input().split()))
            row.append(element)
        matrix2.append(row)

    result = np.add(matrix1, matrix2)
    print("Addition of two matrices = ", result)


def subtract_matrices():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    matrix1 = []
    matrix2 = []

    print("Enter the elements of the first matrix:")
    for i in range(rows):
        row = []
        for j in range(columns):
            element = list(map(int, input().split()))
            row.append(element)
        matrix1.append(row)

    print("Enter the elements of the second matrix:")
    for i in range(rows):
        row = []
        for j in range(columns):
            element = list(map(int, input().split()))
            row.append(element)
        matrix2.append(row)

    result = np.subtract(matrix1, matrix2)
    print("Subtraction of two matrices = ", result)


def multiply_matrices():  # Not Working
    rows1 = int(input("Enter the number of rows of the first matrix: "))
    cols1 = int(input("Enter the number of columns of the first matrix: "))
    rows2 = int(input("Enter the number of rows of the second matrix: "))
    cols2 = int(input("Enter the number of columns of the second matrix: "))

    if cols1 != rows2:
        print("Error: The number of columns of the first matrix should be equal to the number of rows of the second matrix.")
        return

    matrix1 = []
    matrix2 = []

    print("Enter the elements of the first matrix:")
    for i in range(rows1):
        row = []
        for j in range(cols1):
            element = list(map(int, input().split()))
            row.append(element)
        matrix1.append(row)

    print("Enter the elements of the second matrix:")
    for i in range(rows2):
        row = []
        for j in range(cols2):
            element = list(map(int, input().split()))
            row.append(element)
        matrix2.append(row)

    result = np.matmul(matrix1, matrix2)
    print("Multiplication of two matrices = ", result)


def determinant():
    size = int(input("Enter the size of the square matrix: "))

    matrix = []

    print("Enter the elements of the matrix:")
    for i in range(size):
        row = []
        for j in range(size):
            element = int(input())
            row.append(element)
        matrix.append(row)

    result = np.linalg.det(matrix)
    print("Determinant = ", result)


def solve_linear_eq_2_var():
    print("Enter the coefficients of the linear equation in the form 'a1x + b1y = c1'")
    a1 = int(input("Enter coefficient a1: "))
    b1 = int(input("Enter coefficient b1: "))
    c1 = int(input("Enter coefficient c1: "))

    print("Enter the coefficients of the linear equation in the form 'a2x + b2y = c2'")
    a2 = int(input("Enter coefficient a2: "))
    b2 = int(input("Enter coefficient b2: "))
    c2 = int(input("Enter coefficient c2: "))

    result = np.linalg.solve([[a1, b1], [a2, b2]], [c1, c2])
    print("Result: x =", result[0], ", y =", result[1])


def solve_linear_eq_3_var():
    print("Enter the coefficients of the linear equation in the form 'a1x + b1y + c1z = d1'")
    a1 = float(input("Enter coefficient a1: "))
    b1 = float(input("Enter coefficient b1: "))
    c1 = float(input("Enter coefficient c1: "))
    d1 = float(input("Enter coefficient d1: "))

    print("Enter the coefficients of the linear equation in the form 'a2x + b2y + c2z = d2'")
    a2 = float(input("Enter coefficient a2: "))
    b2 = float(input("Enter coefficient b2: "))
    c2 = float(input("Enter coefficient c2: "))
    d2 = float(input("Enter coefficient d2: "))

    print("Enter the coefficients of the linear equation in the form 'a3x + b3y + c3z = d3'")
    a3 = float(input("Enter coefficient a3: "))
    b3 = float(input("Enter coefficient b3: "))
    c3 = float(input("Enter coefficient c3: "))
    d3 = float(input("Enter coefficient d3: "))

    result = np.linalg.solve(
        [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]], [d1, d2, d3])
    print("Result: x =", result[0], ", y =", result[1], ", z =", result[2])


def quadratic_equation():
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print("Result: Two distinct real roots:", root1, "and", root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Result: One real root:", root)
    else:
        real_part = -b / (2 * a)
        imag_part = cmath.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)
        print("Result: Two complex roots:", root1, "and", root2)


def tertiary_equation():
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))
    d = float(input("Enter the coefficient d: "))

    roots = np.roots([a, b, c, d])
    print("Result: ", roots)


def arithmetic_series():
    first_term = float(input("Enter the first term of the series: "))
    common_difference = float(input("Enter the common difference: "))
    index = int(input("Enter the index of the term: "))

    result = first_term + (index - 1) * common_difference
    print("Result: ", result)


def sum_arithmetic_series():
    first_term = float(input("Enter the first term of the series: "))
    last_term = float(input("Enter the last term of the series: "))
    num_terms = int(input("Enter the number of terms: "))

    result = (num_terms / 2) * (first_term + last_term)
    print("Result: ", result)


def factorial():
    n = int(input("Enter a non-negative integer: "))

    if n < 0:
        print("Error: Please enter a non-negative integer.")
        return

    result = np.math.factorial(n)
    print("Result: ", result)


def solve_linear_eq_2_var():
    print("Enter the coefficients of the linear equation in the form 'a1x + b1y = c1'")
    a1 = int(input("Enter coefficient a1: "))
    b1 = int(input("Enter coefficient b1: "))
    c1 = int(input("Enter coefficient c1: "))

    print("Enter the coefficients of the linear equation in the form 'a2x + b2y = c2'")
    a2 = int(input("Enter coefficient a2: "))
    b2 = int(input("Enter coefficient b2: "))
    c2 = int(input("Enter coefficient c2: "))

    result = np.linalg.solve([[a1, b1], [a2, b2]], [c1, c2])
    print("Result: x =", result[0], ", y =", result[1])


def determinant():
    size = int(input("Enter the size of the square matrix: "))

    matrix = []

    print("Enter the elements of the matrix:")
    for i in range(size):
        row = []
        for j in range(size):
            element = int(input())
            row.append(element)
        matrix.append(row)

    result = np.linalg.det(matrix)
    print("Determinant =", result)


def power_iota():
    power = int(input("Enter the power: "))
    # The cmath.exp() method accepts a complex number
    result = cmath.exp(power)
    # and returns the exponential value.
    print("Result: ", result)


def quadratic_equation():
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print("Result: Two distinct real roots:", root1, "and", root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Result: One real root:", root)
    else:
        real_part = -b / (2 * a)
        imag_part = cmath.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)
        print("Result: Two complex roots:", root1, "and", root2)


def tertiary_equation():
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))
    d = float(input("Enter the coefficient d: "))

    roots = np.roots([a, b, c, d])
    print("Result: ", roots)


def arithmetic_series():
    first_term = float(input("Enter the first term of the series: "))
    common_difference = float(input("Enter the common difference: "))
    index = int(input("Enter the index of the term: "))

    result = first_term + (index - 1) * common_difference
    print("Result: ", result)


def sum_arithmetic_series():
    first_term = float(input("Enter the first term of the series: "))
    last_term = float(input("Enter the last term of the series: "))
    num_terms = int(input("Enter the number of terms: "))

    result = (num_terms / 2) * (first_term + last_term)
    print("Result: ", result)


def factorial():
    n = int(input("Enter a non-negative integer: "))

    if n < 0:
        print("Error: Please enter a non-negative integer.")
        return

    result = np.math.factorial(n)
    print("Result: ", result)
