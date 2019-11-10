def PrintNumber(no):
    if(no != 0):
        print(no,end="   ")
        no = no - 1
        PrintNumber(no)

def main():
    value = int(input("Enter the number:"))
    PrintNumber(value)

if __name__ == "__main__":
    main();

