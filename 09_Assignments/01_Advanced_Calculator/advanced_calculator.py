"""
Advanced Console Calculator
Demonstrates: if-elif-else, while loop, for loop, lambda, def functions,
trigonometry, exponentials, factorial, numerical derivative, integration,
root finding, and more.
"""
import math

# ---------------------------------------------------------------
# 1. LAMBDA FUNCTIONS (one-line operations)
# ---------------------------------------------------------------
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
square = lambda x: x ** 2
cube = lambda x: x ** 3
to_rad = lambda d: d * math.pi / 180
to_deg = lambda r: r * 180 / math.pi
percent = lambda part, whole: (part / whole) * 100
celsius_to_f = lambda c: c * 9 / 5 + 32


# ---------------------------------------------------------------
# 2. DEF FUNCTIONS
# ---------------------------------------------------------------
def divide(a, b):
    """Divide a by b, guarding against division by zero."""
    if b == 0:
        return "Error: division by zero"
    return a / b


def power(base, exp):
    """Return base raised to exp."""
    return base ** exp


def sqrt(x):
    """Square root with a check for negative input."""
    if x < 0:
        return "Error: square root of negative number"
    return math.sqrt(x)


def factorial(n):
    """Factorial using a for loop."""
    if n < 0 or n != int(n):
        return "Error: factorial needs a non-negative integer"
    result = 1
    for i in range(2, int(n) + 1):
        result *= i
    return result


def fibonacci(n):
    """First n Fibonacci numbers using a while loop."""
    seq, a, b = [], 0, 1
    while len(seq) < n:
        seq.append(a)
        a, b = b, a + b
    return seq


def is_prime(n):
    """Prime test using a while loop up to sqrt(n)."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def gcd(a, b):
    """Greatest common divisor (Euclid's algorithm, while loop)."""
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    """Least common multiple using gcd."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


# ---- Trigonometry (input in degrees) ----
def trig(func, angle_deg):
    """Evaluate a trig function; angles are in degrees."""
    x = to_rad(angle_deg)
    if func == "sin":
        return math.sin(x)
    elif func == "cos":
        return math.cos(x)
    elif func == "tan":
        if abs(math.cos(x)) < 1e-12:
            return "Error: tan undefined"
        return math.tan(x)
    elif func == "asin":
        return to_deg(math.asin(angle_deg)) if -1 <= angle_deg <= 1 else "Error: domain"
    elif func == "acos":
        return to_deg(math.acos(angle_deg)) if -1 <= angle_deg <= 1 else "Error: domain"
    elif func == "atan":
        return to_deg(math.atan(angle_deg))
    return "Error: unknown trig function"


# ---- Exponential and logarithm ----
def exp_series(x, terms=20):
    """e^x using the Taylor series with a for loop."""
    total = 0
    for n in range(terms):
        total += x ** n / factorial(n)
    return total


def sin_series(x_deg, terms=10):
    """sin(x) using the Taylor series."""
    x = to_rad(x_deg)
    total = 0
    for n in range(terms):
        total += ((-1) ** n) * x ** (2 * n + 1) / factorial(2 * n + 1)
    return total


def log_base(x, base=10):
    """Logarithm of x in any base via change-of-base rule."""
    if x <= 0 or base <= 0 or base == 1:
        return "Error: invalid log input"
    return math.log(x) / math.log(base)


# ---- Combinatorics ----
def nPr(n, r):
    """Permutations: n! / (n-r)!"""
    return factorial(n) // factorial(n - r)


def nCr(n, r):
    """Combinations: n! / (r! (n-r)!)"""
    return factorial(n) // (factorial(r) * factorial(n - r))


# ---------------------------------------------------------------
# 3. CALCULUS AND NUMERICAL METHODS
# ---------------------------------------------------------------
def derivative(f, x, h=1e-5):
    """Central difference: f'(x) ~ (f(x+h) - f(x-h)) / 2h"""
    return (f(x + h) - f(x - h)) / (2 * h)


def second_derivative(f, x, h=1e-4):
    """Three-point formula: f''(x) ~ (f(x+h) - 2f(x) + f(x-h)) / h^2"""
    return (f(x + h) - 2 * f(x) + f(x - h)) / h ** 2


def integrate_trapezoid(f, a, b, n=1000):
    """Definite integral using the trapezoid rule."""
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h


def integrate_simpson(f, a, b, n=1000):
    """Definite integral using Simpson's rule (n must be even)."""
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * f(a + i * h)
    return total * h / 3


def newton_raphson(f, x0, tol=1e-10, max_iter=50):
    """Find a root of f using Newton-Raphson."""
    x = x0
    iteration = 0
    while iteration < max_iter:
        d = derivative(f, x)
        if abs(d) < 1e-12:
            return "Error: zero derivative"
        x_new = x - f(x) / d
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
        iteration += 1
    return "Error: did not converge"


def bisection(f, a, b, tol=1e-10):
    """Find a root of f in [a, b] by repeatedly halving the interval."""
    if f(a) * f(b) > 0:
        return "Error: f(a) and f(b) must have opposite signs"
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


# ---- Polynomials ----
def poly_eval(coeffs, x):
    """coeffs = [a0, a1, a2, ...] -> a0 + a1*x + a2*x^2 ..."""
    result = 0
    for i, c in enumerate(coeffs):
        result += c * x ** i
    return result


def poly_derivative(coeffs):
    """Exact derivative of a polynomial given its coefficients."""
    return [i * coeffs[i] for i in range(1, len(coeffs))] or [0]


def poly_string(coeffs):
    """Pretty-print a polynomial from its coefficients."""
    terms = []
    for i, c in enumerate(coeffs):
        if c == 0:
            continue
        if i == 0:
            terms.append(f"{c}")
        elif i == 1:
            terms.append(f"{c}x")
        else:
            terms.append(f"{c}x^{i}")
    return " + ".join(terms) if terms else "0"


def quadratic(a, b, c):
    """Roots of ax^2 + bx + c = 0 (real or complex) via the discriminant."""
    if a == 0:
        return "Error: not quadratic"
    d = b ** 2 - 4 * a * c
    if d > 0:
        return ((-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a))
    elif d == 0:
        return (-b / (2 * a),)
    return (complex(-b, math.sqrt(-d)) / (2 * a), complex(-b, -math.sqrt(-d)) / (2 * a))


# ---- Statistics ----
def stats(data):
    """Mean, median, variance and standard deviation of a list."""
    n = len(data)
    mean = sum(data) / n
    s = sorted(data)
    median = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
    var = sum((x - mean) ** 2 for x in data) / n
    return {"mean": mean, "median": median, "variance": var, "std": math.sqrt(var)}


# ---------------------------------------------------------------
# 4. FUNCTION PARSER (user types f(x) as text)
# ---------------------------------------------------------------
SAFE = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
SAFE.update({"abs": abs, "pow": pow})


def make_function(expr):
    """Turn text like 'x**2 + sin(x)' into a lambda.

    An equation such as 'x^2 - 2 = 0' or 'x^2 = 2' is also accepted:
    it is rewritten as (left side) - (right side), so the root is the same.
    """
    expr = expr.replace("^", "**")
    if "=" in expr:
        lhs, rhs = expr.split("=", 1)
        if not lhs.strip() or not rhs.strip():
            raise ValueError("equation needs something on both sides of '='")
        expr = f"({lhs}) - ({rhs})"
    return lambda x: eval(expr, {"__builtins__": {}}, {**SAFE, "x": x})


# ---------------------------------------------------------------
# 5. MENU AND MAIN LOOP
# ---------------------------------------------------------------
MENU = """
============ ADVANCED CALCULATOR ============
 1. Basic (+ - * / ^ sqrt)      9. Quadratic solver
 2. Trigonometry               10. Fibonacci / Prime / GCD / LCM
 3. Exponential & Logarithm    11. Statistics
 4. Factorial, nPr, nCr        12. Polynomial derivative
 5. Derivative f'(x)           13. Newton-Raphson root
 6. Second derivative f''(x)   14. Bisection root
 7. Integral (Simpson)         15. History
 8. Unit conversion             0. Exit
=============================================
"""


def read_float(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid number, try again.")


def main():
    """Main menu loop."""
    history = []
    while True:
        print(MENU)
        choice = input("Choose option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            a = read_float("a = ")
            op = input("operator (+ - * / ^ r): ").strip()
            if op == "r":
                res = sqrt(a)
            else:
                b = read_float("b = ")
                if op == "+":
                    res = add(a, b)
                elif op == "-":
                    res = sub(a, b)
                elif op == "*":
                    res = mul(a, b)
                elif op == "/":
                    res = divide(a, b)
                elif op == "^":
                    try:
                        res = power(a, b)
                    except (OverflowError, ZeroDivisionError) as e:
                        res = f"Error: {e}"
                else:
                    res = "Error: unknown operator"
            print("Result:", res)
            history.append(f"basic {a} {op} -> {res}")

        elif choice == "2":
            fn = input("sin/cos/tan/asin/acos/atan: ").strip().lower()
            ang = read_float("value (degrees; for inverse, a ratio): ")
            res = trig(fn, ang)
            print("Result:", res)
            history.append(f"{fn}({ang}) -> {res}")

        elif choice == "3":
            sub_choice = input("1) e^x  2) ln  3) log10  4) log base b: ").strip()
            x = read_float("x = ")
            if sub_choice == "1":
                try:
                    res = math.exp(x)
                    print(f"e^x = {res}   (series approx: {exp_series(x)})")
                except OverflowError:
                    res = "Error: result too large"
            elif sub_choice == "2":
                res = log_base(x, math.e)
            elif sub_choice == "3":
                res = log_base(x, 10)
            elif sub_choice == "4":
                res = log_base(x, read_float("base = "))
            else:
                res = "Error: bad choice"
            print("Result:", res)
            history.append(f"exp/log({x}) -> {res}")

        elif choice == "4":
            n = int(read_float("n = "))
            print(f"{n}! =", factorial(n))
            r = int(read_float("r (for nPr/nCr) = "))
            if 0 <= r <= n:
                print(f"nPr = {nPr(n, r)}   nCr = {nCr(n, r)}")
            else:
                print("nPr/nCr need 0 <= r <= n")
            history.append(f"factorial({n})")

        elif choice in ("5", "6", "7"):
            expr = input("f(x) = ")
            try:
                f = make_function(expr)
                if choice == "5":
                    x = read_float("at x = ")
                    res = derivative(f, x)
                    print(f"f'({x}) = {res:.6f}")
                elif choice == "6":
                    x = read_float("at x = ")
                    res = second_derivative(f, x)
                    print(f"f''({x}) = {res:.4f}")
                else:
                    a = read_float("lower limit a = ")
                    b = read_float("upper limit b = ")
                    res = integrate_simpson(f, a, b)
                    print(f"Integral = {res:.8f}")
                history.append(f"calculus on {expr} -> {res}")
            except Exception as e:
                print("Could not evaluate:", e)

        elif choice == "8":
            print("1) C->F  2) deg->rad  3) rad->deg")
            c = input("choice: ").strip()
            v = read_float("value = ")
            if c == "1":
                print("Result:", celsius_to_f(v))
            elif c == "2":
                print("Result:", to_rad(v))
            elif c == "3":
                print("Result:", to_deg(v))
            else:
                print("Invalid choice")

        elif choice == "9":
            a = read_float("a = ")
            b = read_float("b = ")
            c = read_float("c = ")
            res = quadratic(a, b, c)
            print("Roots:", res)
            history.append(f"quadratic -> {res}")

        elif choice == "10":
            n = int(read_float("n = "))
            print("Fibonacci:", fibonacci(n))
            print("Prime?", is_prime(n))
            m = int(read_float("second number for GCD/LCM = "))
            print("GCD:", gcd(n, m), "  LCM:", lcm(n, m))

        elif choice == "11":
            raw = input("numbers separated by spaces: ")
            try:
                data = [float(t) for t in raw.split()]
                for k, v in stats(data).items():
                    print(f"  {k}: {v:.4f}")
            except (ValueError, ZeroDivisionError):
                print("Invalid data")

        elif choice == "12":
            raw = input("coefficients a0 a1 a2 ... : ")
            try:
                coeffs = [float(t) for t in raw.split()]
                print("p(x)  =", poly_string(coeffs))
                print("p'(x) =", poly_string(poly_derivative(coeffs)))
            except ValueError:
                print("Invalid coefficients")

        elif choice == "13":
            try:
                f = make_function(input("f(x) = "))
                res = newton_raphson(f, read_float("initial guess = "))
                print("Root:", res)
            except Exception as e:
                print("Could not evaluate:", e)

        elif choice == "14":
            try:
                f = make_function(input("f(x) = "))
                res = bisection(f, read_float("a = "), read_float("b = "))
                print("Root:", res)
            except Exception as e:
                print("Could not evaluate:", e)

        elif choice == "15":
            if not history:
                print("No history yet.")
            for i, h in enumerate(history, 1):
                print(f"  {i}. {h}")

        else:
            print("Invalid option, please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
