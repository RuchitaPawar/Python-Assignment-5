def SumDigit(no):
    if no == 0:
        return 0
    return (no % 10 + SumDigit(int(no / 10)))


def main():
    value = int(input("Enter the number:"))
    res = SumDigit(value)
    print(res)

if __name__ == "__main__":
    main();

