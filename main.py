from os import system as run
from sys import exit

from inpt import inpt

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

class introduction:
    def __init__(self):
        print("")
        self.cmd = ""
    def cd(self):
        print("Ok. Beginning Chaper 1: Working with files.")
        print("We will start of with the most basic, cd and ls.")
        print("")
        print("Lets go over cd first.")
        print("cd stands for 'change directory'. This is akin to clicking into a")
        print("folder in a file explorer.")
        print("cd's Windows equivalent is also cd.")
        print("")
        print("Here is how it works:")
        print("cd [directory]")
        print("Now, you try. Try to cd into the directory 'images'")
        self.cmd = input("intro@introsystem:~ $ ")
        while self.cmd != "cd images":
            print("intro@introsystem:~ $")
            print("No, that's not quite right. They way cd works is this:")
            print("'cd <name of directory>'")
        print("intro@introsystem:~/images $")
        print("")
        print(f"Good! The correct awnser was {self.cmd}!")
        print("")
        print("Now, we will go over the next command, ls.")
    def ls(self):
        print("ls stands for 'list'. This is akin to looking at all the files")
        print("and folders in a file browser.")
        print("ls' Windows equivalent is dir.")
        print("Here is how it works:")
        print("ls")
        print("Now, you try. Try to list all the files in the directory'")
        self.cmd = input("intro@introsystem:~/images $ ")
        while self.cmd != "ls":
            print("No, that's not quite right. They way ls works is this:")
            print("'ls'")
        print("coolpic.png              family.jpg")
        print("me.webp")
        print("")
        print(f"Good! The correct awnser was {self.cmd}!")
        print("")
        print("Now, we will go over the next command, cat.")

intro = introduction()

def beginintro(start):
    if (start == "y") or (start == "Y"):
        print("Ok, lets begin!")
        intro.cd()
    else:
        print("Ok. Exiting.")
        exit()

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
