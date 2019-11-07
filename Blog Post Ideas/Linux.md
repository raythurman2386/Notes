# Initial Development Setup for Linux

I am going to show you a very basic initial setup of your development environment for Lambda School.

This tutorial will focus mainly on VS Code and Ubuntu. I will have other guides and walkthroughs for Mac OSX and Windows as well.

Use this walkthrough as a guide till you are more comfortable with these steps and start to customize these instructions to your likings. 

This is a somewhat barebones setup but this will work very well with what you will be doing at Lambda School.

## I will show you how to:
- How to install <a href="https://docs.brew.sh/Homebrew-on-Linux">Homebrew</a>

- How to Install <a href="https://git-scm.com/">Git</a>

- How to Install <a href="https://nodejs.org/en/">Node</a>  

- How to Install <a href="https://code.visualstudio.com/">VS Code</a>

## Install Brew
In this walkthrough I'll be using Homebrew for most of the main installs

Homebrew is a package manager much like NPM is for node and javascript.

As you will see here, homebrew makes it trivial to get a basic dev setup up and running.

and just to be safe, lets install some build-essential tools

```
sudo apt install build-essential curl file git
```

To install brew, run the following commands in your terminal

now essentially there are 5 commands we will be running.
- `sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"`

- `test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)`

- `test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)`

- `test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile`

- `echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile`

One by one, run those commands

now you should have brew installed onto your system

### Brew Packages
If you would like to check out the many brew packages you can install check out those lists here: https://formulae.brew.sh/

## Install Git
- brew install git

### Basic Git setup

```
git config --global user.name YourNameHere
git config --global user.email YourEmailHere
git config --global core.autocrlf false
```
There are a few other config settings you could add, but these will be the ones to get you up and running. 

Feel free to check out the docs on the other config options.

### Creating a new SSH Key
If you do not already have an SSH Key we will set one up right now.

```
ssh-keygen -t rsa -b 4096 -C "yourEmailHere"
```

now to copy the file and add it to github

```
cp ~/.ssh/id_rsa.pub
```

Or display your key and copy it from the terminal with: 

```
cat ~/.ssh/id_rsa.pub
```


### Basic Git Lambda Workflow

## Install Node
- brew install node

## Installing VS Code
Ok, finally to the fun part.
Lets install <a href="https://code.visualstudio.com/">VS Code</a>

### Useful Shortcuts
- Toggle Sidebar      Ctrl + B
- Command Pallette    Ctrl + Shift + P
- File Switcher       Ctrl + P
- Terminal            Ctrl + `
- Settings            Ctrl + ,
- Previous file       Ctrl + P + P
- focus Sidebar       Cmd/Ctrl + 0
- focus Editor        Cmd/Ctrl + 1
- Open Source Control Ctrl + Shift + G
- Move Line           Alt + Down/Up Arrow
- Delete Line         Ctrl + Shift + k

### Extensions
- Prettier
- Bracket Pair Colorizer
- Live Server
- Material Icon && theme
- Quokka
- eslint

## Honorable Mentions
  - Github Desktop
  - Fira Code
  - Cascadia Code