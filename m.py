from mathoperations import MathOperations

def main():
    num1 = 10
    num2 = 5

    calculator = MathOperations(num1, num2)

    print(f"Addition: {calculator.add()}")
    print(f"Subtraction: {calculator.subtract()}")
    

if __name__ == "__main__":
    main()