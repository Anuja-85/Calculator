import calculator


def Menu():

    menuItems = [
        "Add", "Subtract", "Multiply", "Divide", "Add 2 complex numbers", "Subtract 2 complex numbers", "Multiply 2 complex numbers", "Power of a number", "Power of iota", "Addition of 2 matrices", "Subtraction of 2 matrices", "Multiplication of 2 matrices", "Determinant of a matrix", "Solve linear equation in 2 variables", "Solve linear equation in 3 variables", "Find roots of quadratic equation", "Find roots of tertiary equation", "Find nth element of arithmetic series", "Find sum of first n elements of arithmetic series", "Evaluate factorial of n"
        "Exit"
    ]
    print("---- Calculator Menu ----")

    for i in range(0, len(menuItems)):
        print(f"ord({i+1+65}) menuItems[i]. ")


# Main program
while True:

    Menu()
    choice = input("Enter your choice (A-T or X to exit): ")

    if choice == "A":
        add()
    elif choice == "B":
        subtract()
    elif choice == "C":
        multiply()
    elif choice == "D":
        divide()
    elif choice == "E":
        add_complex()
    elif choice == "F":
        subtract_complex()
    elif choice == "G":
        multiply_complex()
    elif choice == "H":
        power()
    elif choice == "I":
        power_iota()
    elif choice == "J":
        add_matrices()
    elif choice == "K":
        subtract_matrices()
    elif choice == "L":
        multiply_matrices()
    elif choice == "M":
        determinant()
    elif choice == "N":
        solve_linear_eq_2_var()
    elif choice == "O":
        solve_linear_eq_3_var()
    elif choice == "P":
        quadratic_equation()
    elif choice == "Q":
        tertiary_equation()
    elif choice == "R":
        arithmetic_series()
    elif choice == "S":
        sum_arithmetic_series()
    elif choice == "T":
        factorial()
    elif choice == "X":
        print("Exiting the calculator...")
        break
    else:
        print("Invalid choice! Please select a valid option from A-T or X to exit.")
