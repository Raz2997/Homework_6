class AddCommand:
    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
            print(f"Result: {a + b}")
        except ValueError:
            print("Invalid input! Please enter two numbers.")

class SubtractCommand:
    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
            print(f"Result: {a - b}")
        except ValueError:
            print("Invalid input! Please enter two numbers.")

class MultiplyCommand:
    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
            print(f"Result: {a * b}")
        except ValueError:
            print("Invalid input! Please enter two numbers.")

class DivideCommand:
    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
            if b == 0:
                print("Error: Cannot divide by zero!")
            else:
                print(f"Result: {a / b}")
        except ValueError:
            print("Invalid input! Please enter two numbers.")
