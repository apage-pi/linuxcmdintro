def beginintro(start):
    if (start == "y") or (start == "Y"):
        print("Ok, lets begin!")

def main(): 
    print("Welcome to the Linux Commands Intro! This is a short guide that tours you through basic commands")
    print("and their Windows equivalents, if any.")
    print("")
    print("Here is how to enter input into a command line: Type your response and press enter.")
    begin = input("Shall we begin (y/n)? ")
    beginintro(begin)

if __name__ == "__main__":
    main()
