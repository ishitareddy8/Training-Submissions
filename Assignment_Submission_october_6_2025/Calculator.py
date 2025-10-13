def calc(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    raise ValueError("Unsupported operation. Use + - * /")

if __name__ == "__main__":
    a = float(input("Enter first number: "))
    op = input("Enter operation (+ - * /): ").strip()
    b = float(input("Enter second number: "))
    print("Result:", calc(a, b, op))

