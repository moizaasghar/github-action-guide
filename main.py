from src.calculator import calculator

def main():
    calc = calculator()
    print(calc.add(5, 3))
    print(calc.subtract(5, 3))
    print(calc.multiply(5, 3))
    print(calc.divide(5, 0))

if __name__ == "__main__":
    main()