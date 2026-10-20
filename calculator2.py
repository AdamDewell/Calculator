def add(a, b):
        return a + b

def subtract(a, b):
        return a - b

def multiply(a, b):
        return a * b

def divide(a, b):
        return a / b
def main(): 
        while True:
                a = float(input("First number: "))
                op = input("Operator: ")
                b = float(input("Second number: "))
                if op == "+": 
                        print(f"Result: {add(a, b)}")
                elif op == "-":
                        print(f"Result: {subtract(a, b)}")
                elif op == "*":
                        print(f"Result: {multiply(a, b)}")
                elif op == "/":
                        print(f"Result: {divide(a, b)}")
                else:
                        print(f"Unkown operator: {op}")

if __name__ == "__main__":
        main()
