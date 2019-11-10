def Factorial(no):
    if no == 0 or no == 1:
        return 1
    else:
        return no * Factorial(no-1)

def main():
    value = int(input("Enter the number:"))
    res = Factorial(value)
    print("Factorial of number is:",res)

if __name__ == "__main__":
    main();

