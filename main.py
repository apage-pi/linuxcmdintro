from os import system as run
from sys import exit
from time import sleep

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
        exit()


class introduction:

    def __init__(self):
        self.cmd = ""

    def start(self):
        self.files = self.file()
        self.sysadmin = self.SysAdmin()
        self.files.cd()
        self.files.ls()
        self.files.cat()
        self.files.touch()
        self.files.mv()
        self.files.less()
        self.files.nano()
        self.files.rm()
        self.files.grep()
        self.sysadmin.apt()
        self.sysadmin.lynx()
        self.sysadmin.man()

    class file:

        def __init__(self):
            self.cmd = ""

        def cd(self):
            print("Ok. Beginning Chaper 1: Working with files.")
            print("We will start of with the most basic, cd and ls.")
            print("")
            print("Lets go over cd first.")
            print(
                "cd stands for 'change directory'. This is akin to clicking into a"
            )
            print("folder in a file explorer.")
            print("cd's Windows equivalent is also cd.")
            print("")
            print("Here is how it works:")
            print("cd [directory]")
            print("Now, you try. Try to cd into the directory 'images'")
            self.cmd = input("intro@introsystem:~ $ ")
            while self.cmd != "cd images":
                print("No, that's not quite right. They way cd works is this:")
                print("'cd <name of directory>'")
                self.cmd = input("intro@introsystem:~ $ ")
            print("intro@introsystem:~/images $")
            sleep(1.5)
            print("")
            print(f"Good! The correct awnser was {self.cmd}!")
            print("")
            print("Now, we will go over the next command, ls.")
            sleep(1.5)

        def ls(self):
            print(
                "ls stands for 'list'. This is akin to looking at all the files"
            )
            print("and folders in a file browser.")
            print("ls' Windows equivalent is dir.")
            print("Here is how it works:")
            print("ls")
            print("Now, you try. Try to list all the files in the directory")
            self.cmd = input("intro@introsystem:~/images $ ")
            while self.cmd != "ls":
                print("No, that's not quite right. They way ls works is this:")
                print("'ls'")
                self.cmd = input("intro@introsystem:~/images $ ")
            print("coolpic.png              family.jpg")
            print("me.webp")
            sleep(1.5)
            print("")
            print(f"Good! The correct awnser was {self.cmd}!")
            print("")
            print("Now, we will go over the next command, cat.")
            sleep(1.5)

        def cat(self):
            print(
                "cat stands for 'concatenate'. This is akin to opening a read-only file,"
            )
            print("but in a viewer wihout a scrollbar")
            print("cat's Windows equivalent is type.")
            print("Here is how it works:")
            print("cat <file>")
            print(
                "Now, you try. Try to find the content in the document 'file.txt'"
            )
            self.cmd = input("intro@introsystem:~/documents $ ")
            while self.cmd != "cat file.txt":
                print("No, that's not quite right. They way ls works is this:")
                print("'cat <file>'")
                self.cmd = input("intro@introsystem:~/documents $ ")
            print("Hello World!")
            sleep(1.5)
            print("")
            print(f"Good! The correct awnser was {self.cmd}!")
            print("")
            print("Now, we will go over the next command, touch.")
            sleep(1.5)

        def touch(self):
            print(
                "touch dosent stand for anything. It is akin to updating the timestamp on a file."
            )
            print(
                "touch will also create a file if it does not exist yet, making it useful."
            )
            print(
                "touch's Windows equivalent is type (only for creating files, though)."
            )
            print("Here is how it works:")
            print("touch <file>")
            print("Now, you try. Try to create the file 'file2.txt'")
            self.cmd = input("intro@introsystem:~/documents $ ")
            while self.cmd != "touch file2.txt":
                print("No, that's not quite right. They way ls works is this:")
                print("'touch <file>'")
                self.cmd = input("intro@introsystem:~/documents $ ")
            sleep(1.5)
            print("")
            print(f"Good! The correct awnser was {self.cmd}!")
            print("")
            print("Now, we will go over the next command, mv.")
            sleep(1.5)

        def mv(self):
            print(
                "mv stands for move. It is akin to dragging and dropping a file,"
            )
            print("having it move, or renamig.")
            print("mv can also be used to rename, making it more useful.")
            print("mv's Windows equivalent is move.")
            print("Here is how it works:")
            print("mv <file> <new location/name> ")
            print(
                "Now, you try. Try to rename the file 'fileyes.txt' to 'fileno.txt'"
            )
            self.cmd = input("intro@introsystem:~/documents $ ")
            while self.cmd != "mv fileyes.txt fileno.txt":
                print("No, that's not quite right. They way ls works is this:")
                print("'mv <file> <new location/name> '")
                self.cmd = input("intro@introsystem:~/documents $ ")
            sleep(1.5)
            print("")
            print(f"Good! The correct awnser was {self.cmd}!")
            print("")
            print("Now, we will go over the next command, less.")
            sleep(1.5)

        def less(self):
            print(
                "less does not stand for anything. It is akin to opening a read-only file,"
            )
            print("but in a viewer with a scroll bar")
            print("less's Windows equivalent is more.")
            print("Here is how it works:")
            print("less <file>")
            print("Now, you try. Try to execute less on the file 'hi.txt'")
            print("To exit less, press q.")
            self.cmd = input("intro@introsystem:~/documents $ ")
            while self.cmd != "less hi.txt":
                print("No, that's not quite right. They way ls works is this:")
                print("'less <file>'")
                self.cmd = input("intro@introsystem:~/documents $ ")
            run("less ./hi.txt")
            sleep(1.5)
            print("")
            print(f"Good! The correct awnser was {self.cmd}!")
            print("")
            print("Now, we will go over the next command, nano.")
            sleep(1.5)

        def nano(self):
            print(
                "nano does not stand for anything. It is akin to opening a file in a"
            )
            print(
                "text editor, or creating a new one and having it open in an editor."
            )
            print("nano's Windows equivalent is edit.")
            print("Here is how it works:")
            print("nano <file>")
            print("Now, you try. Try to execute nano on the file 'myfile.txt'")
            print("To exit nano, press ctrl+X, then y, then enter.")
            print("Write a file with whatever you want in it ok?")
            sleep(3.5)
            self.cmd = input("intro@introsystem:~/documents $ ")
            while self.cmd != "nano myfile.txt":
                print("No, that's not quite right. They way ls works is this:")
                print("'nano <file>'")
                self.cmd = input("intro@introsystem:~/documents $ ")
            run("nano myfile.txt")
            print("Here is what you wrote! :")
            run("cat myfile.txt")
            sleep(1.5)
            print("")
            print(f"Good! The correct awnser was {self.cmd}!")
            print("")
            print("Now, we will go over the next command, rm.")
            sleep(1.5)

        def rm(self):
            print(
                "rm stands for remove. It is akin to permanently deleting a file or folder"
            )
            print("rm's Windows equivalent is del.")
            print("Here is how it works:")
            print("For a file: rm <file>")
            print("For a folder: rm -r <folder>")
            print("Now, you try. Try to delete the file 'randomfile.txt'")
            self.cmd = input("intro@introsystem:~/documents $ ")
            while self.cmd != "rm randomfile.txt":
                print("No, that's not quite right. They way ls works is this:")
                print("'rm <file>'")
                self.cmd = input("intro@introsystem:~/documents $ ")
            sleep(1.5)
            print("")
            print(f"Good! The correct awnser was {self.cmd}!")
            print("")
            print("Now, we will go over the next command, grep.")
            sleep(1.5)

        def grep(self):
            print(
                "grep stands for global regular expression parser."
            )
            print("It is akin to using the 'find all' command in a text editor")
            print("grep's Windows equivalent is findstr.")
            print("Here is how it works:")
            print("grep <expression> <file>")
            print("Now, you try. Try to take out all occurences of 'hi' in hihello.txt")
            print("here is what hihello.txt looks like:")
            run("cat hihello.txt")
            self.cmd = input("intro@introsystem:~/documents $ ")
            while self.cmd != "grep hi hihello.txt":
                print("No, that's not quite right. They way ls works is this:")
                print("'rm <file>'")
                self.cmd = input("intro@introsystem:~/documents $ ")
            run("grep hi hihello.txt")
            sleep(1.5)
            print("")
            print(f"Good! The correct awnser was {self.cmd}!")
            print("")
            print("Now, we go to chapter 2, System Administration-Related.")
            sleep(1.5)
    class SysAdmin():
        def __init__(self):
            self.cmd = ""
        def apt(self):
            print("")
            print("apt stands for Advanced Package Tool. It is equivalent to opening the app store")
            print("and updating or installing stuff.")
            print("apt's Windows equivalent on the command line is winget")
            print("apt is more complex than any other command that we have gone through so far.")
            print("The first part is updating the list of software, the repositories.")
            print("It is done via sudo apt update.")
            sleep(3)
            print("Then to update the system, use sudo apt upgrade.")
            print("To install something, use sudo apt install <package>.")
            sleep(3)
            print("Not all linux distrobutions use apt. We use it here because the biggest")
            print("and most beginner-friendly distros (distrobutions) use it.")
            sleep(3)
            print("Some exceptions are:")
            print("Fedora -- dnf")
            print("CentOS & RHEL -- yum")
            print("openSUSE -- zypper")
            print("Arch Linux -- pacman")
            sleep(3)
            print("We won't go over this one because it is too complex for a simple demo.")
            print("Lets move on, shall we?")
            sleep(5)
        def lynx(self):
            print("")
            print("Lynx is a web browser, in the terminal")
            print("It is very basic, only loading basic HTML, but it works.")
            print("It support downloads as well.")
            print("We won't go pver it, but you can research and learn about it on your")
            print("own time.")
            print("We will move on to the final main topic.")
            sleep(3)
        def man(self):
            print("")
            print("man essentially the program that contains 'manuals' for each command")
            print("It works like the less command does.")
            print("Any good package will have a manpage to help with usage.")
            print("We won't go pver it, but you can research and learn about it on your")
            print("own time.")
            print("We will finally wrap things up.")
            sleep(3)
    class outro:
        def __init__(self) -> None:
            self.cmd = ""
        def out(self):
            print("")
            print("")
            print("I hope this has given you an idea of what people actually")
            print("do in a terminal, its not always hacking.")
            print("Some people just use it because it is mroe efficient to use.")
            print("Some people use it because it is more lightweight.")
            print("Some people use it because it is the only way to do some things.")
            print("macOS and Windows have their own terminals.")
            sleep(3)
            print("macOS's is named terminal. Windows has two: the classic Command Prompt,")
            print("and the newer, more advanced, Powershell.")
            print("If you want to try these Linux commands out, try to find a")
            print("beginner-friendly linux distro, preferrably based on Debian, such as:")
            print("KDE Neon, Linux Mint, Ubuntu, Zorin OS, and, if you are a it more advanced")
            print("with system management, Debian Stable itself, which (If using Docker),")
            print("is what is program is running on.")
            print("For now, goodbye.")
            sleep(5)
            print("")
            print("")
            print("Check this project out at: https://github.com/apage-pi/linuxcmdintro")
            print("Find some more of my projects here: https://github.com/apage-pi")
            print("")
            sleep(1)
            print("Goodbye!")
            exit()


intro = introduction()
outro = introduction.outro()


def beginintro(start):
    while (start != "Y") or (start != "y") or (start != "N") or (start != "n"):
        if (start == "y") or (start == "Y"):
            print("Ok, lets begin!")
            print(
                "Remember, you can exit at any time by pressing Ctrl + C (Cmd + C on macOS)"
            )
            intro.start()
            outro.out()

        elif (start == "N") or (start == "n"):
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
