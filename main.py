from inpt import inpt


def beginintro(start):
    if (start == "y") or (start == "Y"):
        print("Ok, lets begin!")


def input(prnt):
    try:
        val = inpt(prnt)
        return val
    except EOFError:
        print(
            "Whoops! This interpreter instance does not support input/interactive!"
        )
        print(
            'If you are running with Docker, run the image with the flag "-it".'
        )


def main():
    print(
        "Welcome to the Linux Commands Intro! This is a short guide that tours you"
    )
    print("through basic commands and their Windows equivalents, if any.")
    print("")
    print(
        "Here is how to enter input into a command line: Type your response and"
    )
    print("press enter.")
    begin = input("Shall we begin (y/n)? ")
    beginintro(begin)


if __name__ == "__main__":
    main()
