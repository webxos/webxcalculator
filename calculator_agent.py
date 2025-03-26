def calculator_agent(operation, num1, num2):
    """
    Basic calculator agent that performs arithmetic operations
    """
    try:
        num1 = float(num1)
        num2 = float(num2)
        
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        else:
            return "Error: Invalid operation"
    except ValueError:
        return "Error: Please enter valid numbers"

# Simple command-line interface for testing
if __name__ == "__main__":
    print("Calculator Agent - Available operations: add, subtract, multiply, divide")
    op = input("Enter operation: ").lower()
    n1 = input("Enter first number: ")
    n2 = input("Enter second number: ")
    result = calculator_agent(op, n1, n2)
    print(f"Result: {result}")
