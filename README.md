# Interactive Intro to Linux Commands #
## A school project by Adam Page #
### About ###
This is an Interactive Introduction to Linux commands and their Windows counterparts. 
It was originally made for a school project but decided to post it to the internet so others could use it.
Commands/Programs Demonstrated w/ syntax:

FIle-based:
- ls
- cd
- echo
- touch
- nano
- cat
- less
- grep
- mv
- rm

System Administration-based:
- apt/dnf/yum/pacman/zypper (not demonstrated, but showed how to use)
- lynx (mentioned, not demonstrated)
- man

### Running ###

Dependencies if running the exe or main.py:
nano, less, python3.11

There are four ways to run this:
1. Download the executable and run it (Linux only) 
2. Download repo, run main.py (Linux only)
3. Build a docker image manually, and run it with -it
4. Pull the docker image, and run it with -it

Docker instructions:

If building manually:
- Clone repo
- Open terminal in repo
- Run `docker build -t onedrive365/linuxcmdintro .`
- After that is done, run `docker run -it --rm onedrive365/linuxcmdintro`

If using the prebuilt image:
- Run `docker pull onedrive365/linuxcmdintro`
- Run `docker run -it --rm onedrive365/linuxcmdintro`

Hope you have fun with this!
