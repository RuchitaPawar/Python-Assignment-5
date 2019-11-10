def Pattern(no):
    if(no != 0):
        print("*",end="   ")
        no = no - 1
        Pattern(no)

def main():
    value = int(input("Enter the number:"))
    Pattern(value)

if __name__ == "__main__":
    main();

