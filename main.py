import math

system = input('\n[1] Accuracy Numerical Calculation '
               '\n[2] Interpolation and Polynomial Approximation'
               '\n[3] Numerical Differentiation'
               '\n[4] Numerical Integration'
               '\nOption: ')

if system == "1":
    method = input('[a] mclaurin formula [b] finding error: ')

    if method == "a":
        func = input("Enter a function in terms of x: ")
        n = int(input("Enter the number of terms to approximate: "))
        dp = int(input("Enter the number of decimal places to round to: "))

        # Maclaurin Series Calculation
        def maclaurin_series(func, n):
            sum = 0
            for i in range(n+1):
                f = eval(func.replace('x', '0'))
                d = eval(func.replace('x', '0.0'))
                sum += (d/math.factorial(i)) * (0**i)
                func = func.replace('x', '(x-0)')
            return sum

        maclaurin_series = maclaurin_series(func, n)
        print("Maclaurin Series: ", maclaurin_series)
        
    if method == "b":
            av_round = round(abs(maclaurin_series), dp)
            abs_error_round = round(abs(eval(func.replace('x', '0')) - av_round), dp)
            rel_error_round = round(abs_error_round/abs(eval(func.replace('x', '0'))), dp)
            print("Absolute Value - Rounding: ", av_round)
            print("Absolute Error - Rounding: ", abs_error_round)
            print("Relative Error - Rounding: ", rel_error_round)

            # Chopping
            av_chop = float(str(abs(maclaurin_series))[:dp+2])
            abs_error_chop = abs(eval(func.replace('x', '0')) - av_chop)
            rel_error_chop = abs_error_chop / abs(eval(func.replace('x', '0')))
            print("Absolute Value - Chopping: ", av_chop)
            print("Absolute Error - Chopping: ", abs_error_chop)
            print("Relative Error - Chopping: ", rel_error_chop)
            
if system == "2":
    method = input('[a] Bisection Method [b] Secant Method: ')

    if method == "a":
        choice = input('[1] Tolerance Error [2] Iteration: ')

        if choice == "1":
            def bisection_method(f_str, a, b, e):
                f = lambda x: eval(f_str.replace('x', str(x)))

                iteration = 1
                print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<10} {:<10}".format(
                    "Iteration", "a", "b", "c", "f(c)", "|a-b|", "< error"))
                print("-" * 85)

                while abs(a - b) > e:
                    c = (a + b) / 2
                    fc = f(c)
                    print("{:<10} {:<10.6f} {:<10.6f} {:<10.6f} {:<15.10f} {:<10.6f} {:<10.6f}".format(
                        iteration, a, b, c, fc, abs(a - b), e))

                    if fc == 0:
                        return c
                    elif f(a) * fc < 0:
                        b = c
                    else:
                        a = c
                    iteration += 1

                root = (a + b) / 2
                print("{:<10} {:<10.6f} {:<10.6f} {:<10.6f} {:<15.10f} {:<10.6f} {:<10.6f}".format(
                    iteration, a, b, root, f(root), abs(a - b), e))
                print('Cn =', root)
                print('f(Cn) =', f(root))
                return root


            f_str = input("Enter your function: ")
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            e = float(input("Enter the tolerance: "))

            root = bisection_method(f_str, a, b, e)

        elif choice == "2":
            def bisection_method(f_str, a, b, n):
                f = lambda x: eval(f_str.replace('x', str(x)))

                print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                    "Iteration", "a", "b", "Cn", "f(c)", "|a-b|"))

                if f(a) * f(b) >= 0:
                    print("The method may not converge.")
                else:
                    c = (a + b) / 2
                    fc = f(c)
                    e = abs(a - b)
                    print("{:<10} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f}".format(
                        0, a, b, c, fc, e))

                    if fc == 0:
                        return c

                for i in range(n):
                    c = (a + b) / 2
                    fc = f(c)
                    e = abs(a - b)

                    print("{:<10} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f}".format(
                        i + 1, a, b, c, fc, e))

                    if fc == 0:
                        return c

                    if f(a) * fc < 0:
                        b = c
                    else:
                        a = c

                root = (a + b) / 2
                print('Cn =', c)
                print('f(Cn) =', fc)
                return root


            f_str = input("Enter your function: ")
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            n = int(input("Enter number of iterations: "))
            root = bisection_method(f_str, a, b, n)

    elif method == "b":
        choice = input('[1] Tolerance Error [2] Iteration: ')

        if choice == "1":
            def secant_method(f_str, x0, x1, e):
                f = lambda x: eval(f_str.replace('x', str(x)))

                print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<10} {:<10} {:<10}".format(
                    "Iteration", "Xn-1", "Xn", "f(Xn-1)", "f(Xn)", "Xn+1", "|Xn+1 - Xn|", "< error"))

                n = 1
                while True:
                    fx0 = f(x0)
                    fx1 = f(x1)
                    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
                    print("{:<10} {:<10.6f} {:<10.6f} {:<10.6f} {:<15.10f} {:<10.6f} {:<10.6f} {:<10.6f}".format(
                        n, x0, x1, fx0, fx1, x2, abs(x2 - x1), e))

                    if abs(x2 - x1) < e:
                        cn = f(x2)
                        print("f(Cn) =", cn)
                        return x2
                    x0 = x1
                    x1 = x2
                    n += 1


            f_str = input("Enter function: ")
            x0 = float(input("Enter Xn-1: "))
            x1 = float(input("Enter Xn: "))
            e = float(input("Enter tolerance error: "))
            root = secant_method(f_str, x0, x1, e)
            print("Cn =", root)

        elif choice == "2":
            def secant_method(f_str, x0, x1, n):
                f = lambda x: eval(f_str.replace('x', str(x)))

                print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<10} {:<10}".format(
                    "Iteration", "Xn-1", "Xn", "f(Xn-1)", "f(Xn)", "Xn+1", "|Xn+1 - Xn|"))

                for i in range(n):
                    fx0 = f(x0)
                    fx1 = f(x1)
                    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
                    print("{:<10} {:<10.6f} {:<10.6f} {:<10.6f} {:<15.10f} {:<10.6f} {:<10.6f}".format(
                        i + 1, x0, x1, fx0, fx1, x2, abs(x2 - x1)))

                    if abs(x2 - x1) < 1e-6:
                        cn = f(x2)
                        print("f(Cn) =", cn)
                        return x2
                    x0 = x1
                    x1 = x2

                print("Cn =", x2)
                return x2


            f_str = input("Enter function: ")
            x0 = float(input("Enter Xn-1: "))
            x1 = float(input("Enter Xn: "))
            n = int(input("Enter number of iterations: "))
            root = secant_method(f_str, x0, x1, n)
            print("Cn =", root)

elif system == "3":
    method = input('[a] user defined [b] pre defined: ')

    if method == "a":
        def newton_interpolation(n, x, y, x_interpolate):

            divided_difference = [[0 for i in range(n)] for j in range(n)]

            for i in range(n):
                divided_difference[i][0] = y[i]

            for j in range(1, n):
                for i in range(n - j):
                    if x[i + j] != x[i]:
                        divided_difference[i][j] = (divided_difference[i + 1][j - 1] - divided_difference[i][j - 1]) / (
                                    x[i + j] - x[i])

            interpolated_value = divided_difference[0][0]
            pn_x = f"{divided_difference[0][0]:.0f}"
            for i in range(1, n):
                term = divided_difference[0][i]
                for j in range(i):
                    term *= (x_interpolate - x[j])
                interpolated_value += term
                pn_x += f" + {term:.0f}"
                for j in range(i):
                    pn_x += f"(x - {x[j]:.0f})"

            return interpolated_value, pn_x


        n = int(input("Enter number of sample points: "))
        x = []
        y = []
        for i in range(n):
            x_val = float(input(f"Enter x{i}: "))
            y_val = float(input(f"Enter y{i}: "))
            x.append(x_val)
            y.append(y_val)
        x_interpolate = float(input("Enter value of x to interpolate:"))

        interpolated_value, pn_x = newton_interpolation(n, x, y, x_interpolate)

        print(f"The interpolated value at x = {x_interpolate} is {interpolated_value:.0f}.")
        print(f"The polynomial function pn(x) = {pn_x}.")

    elif method == "2":
        def newton_interpolation(n, x, y, x_interpolate):

            divided_difference = [[0 for i in range(n)] for j in range(n)]

            for i in range(n):
                divided_difference[i][0] = y[i]

            for j in range(1, n):
                for i in range(n - j):
                    if x[i + j] != x[i]:
                        divided_difference[i][j] = (divided_difference[i + 1][j - 1] - divided_difference[i][j - 1]) / (
                                    x[i + j] - x[i])

            interpolated_value = divided_difference[0][0]
            pn_x = f"{divided_difference[0][0]:.0f}"
            for i in range(1, n):
                term = divided_difference[0][i]
                for j in range(i):
                    term *= (x_interpolate - x[j])
                interpolated_value += term
                pn_x += f" + {term:.0f}"
                for j in range(i):
                    pn_x += f"(x - {x[j]:.0f})"

            return interpolated_value, pn_x


        n = 7
        x = [1.37, 1.29, 1.31, 1.33, 1.36, 1.34, 1.30, 1.33, 1.46, 1.29]
        y = [1.20, 1.22, 1.25, 1.27, 1.30, 1.35, 1.33, 1.29, 1.20, 1.28]

        x_interpolate = float(input("Enter value of x to interpolate:"))

        interpolated_value, pn_x = newton_interpolation(n, x, y, x_interpolate)

        print(f"The interpolated value at x = {x_interpolate} is {interpolated_value:.0f}.")
        print(f"The polynomial function pn(x) = {pn_x}.")

elif system == "4":
   import math

def f(x):
    """Define the function f(x)"""
    return math.exp(2 * x)

def convert_expression(expression):
    """Convert the input expression to Python syntax"""
    expression = expression.replace('^', '**')
    expression = expression.replace('e', 'math.exp(1)')
    expression = expression.replace('sin', 'math.sin')
    expression = expression.replace('cos', 'math.cos')
    expression = expression.replace('tan', 'math.tan')
    expression = expression.replace('log', 'math.log')
    expression = expression.replace('sqrt', 'math.sqrt')
    expression = expression.replace('pi', 'math.pi')
    expression = expression.replace('/', ' / ')

    return expression

def trapezoidal_rule(f, a, b, n):
    """Trapezoidal Rule"""
    h = (b - a) / n
    results = []
    for i in range(n + 1):
        xi = a + i * h
        try:
            fxi = f(xi)
        except (ValueError, ZeroDivisionError, OverflowError, TypeError):
            fxi = float('nan')  
        if i == 0 or i == n:
            Ti = fxi
        else:
            Ti = 2 * fxi
        results.append((i, xi, fxi, Ti))
    sum_Ti = sum(Ti for i, xi, fxi, Ti in results)
    approx_integral = (h / 2) * sum_Ti
    return results, approx_integral

def simpsons(f, a, b, n):
    """Simpson's 1/3 Rule"""
    h = (b - a) / n
    results = []
    for i in range(n + 1):
        xi = a + i * h
        try:
            fxi = f(xi)
        except (ValueError, ZeroDivisionError, OverflowError, TypeError):
            fxi = float('nan')  
        if i == 0 or i == n:
            Si = fxi
        elif i % 2 == 1:
            Si = 4 * fxi
        else:
            Si = 2 * fxi
        results.append((i, xi, fxi, Si))
    sum_Si = sum(Si for i, xi, fxi, Si in results)
    approx_integral = (h / 3) * sum_Si
    return results, approx_integral


def check_convergence_difference(approximations, threshold):
    for i in range(1, len(approximations)):
        difference = abs(approximations[i] - approximations[i-1])
        if difference < threshold:
            return True
    return False

def check_convergence_relative_change(approximations, threshold):
    for i in range(1, len(approximations)):
        relative_change = abs(approximations[i] - approximations[i-1]) / abs(approximations[i-1])
        if relative_change < threshold:
            return True
    return False


while True:
    try:

        f_input = input("Enter the function f(x): ")
        a_input = float(input("Enter the lower limit (a): "))
        b_input = float(input("Enter the upper limit (b): "))
        n_input = int(input("Enter the number of intervals: "))

    
        def_input = lambda x: eval(convert_expression(f_input))

        
        trapezoidal_results, trapezoidal_approx_integral = trapezoidal_rule(def_input, a_input, b_input, n_input)
     
        simpsons_results, simpsons_approx_integral = simpsons(def_input, a_input, b_input, n_input)


        delta_x = (b_input - a_input) / n_input
        print("\nΔx:", delta_x)

        
        print("\nTrapezoidal Rule Table:")
        print("i\t xi\t\t f(xi)\t\t\t\t Ti")
        for i, xi, fxi, Ti in trapezoidal_results:
            print(f"{i}\t {xi}\t {fxi:.14f}\t {Ti:.14f}")
        
        print("ΣTi:", sum(Ti for i, xi, fxi, Ti in trapezoidal_results))
      
        print("T:", trapezoidal_approx_integral)

       
        print("\nSimpson's 1/3 Rule Table:")
        print("i\t xi\t\t f(xi)\t\t\t\t Si")
        for i, xi, fxi, Si in simpsons_results:
            print(f"{i}\t {xi}\t {fxi:.14f}\t {Si:.14f}")
        print("ΣSi:", sum(Si for i, xi, fxi, Si in simpsons_results))
        print("S:", simpsons_approx_integral)

        approximations = [trapezoidal_approx_integral, simpsons_approx_integral]
        threshold_difference = 1e-6  
        threshold_relative_change = 1e-6  

        if check_convergence_difference(approximations, threshold_difference):
            print("The integral is convergent based on absolute difference check.")
        else:
            print("The integral is divergent based on absolute difference check.")

        if check_convergence_relative_change(approximations, threshold_relative_change):
            print("The integral is convergent based on relative change check.")
        else:
            print("The integral is divergent based on relative change check.")

    except (ValueError, ZeroDivisionError, OverflowError, TypeError):
        print("The integral is undefined or cannot be evaluated.")

    repeat = input("\nDo you want to calculate another integral? (y/n): ")
    if repeat.lower() != "y":
        break

else:
    print("Invalid option. Please try again.")
