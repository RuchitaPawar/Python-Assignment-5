def PrintNumber(no,start):
    if(start <= no):
        print(start,end="   ")
        start = start + 1
        PrintNumber(no,start)


def main():
    value = int(input("Enter the number:"))
    start =1
    PrintNumber(value,start)

if __name__ == "__main__":
    main();

