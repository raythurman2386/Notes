# Initial Development Setup for Mac

I am going to show you a very basic initial setup of your development environment for Lambda School.

This tutorial will focus mainly on VS Code and Mac OSX. I will have other guides and walkthroughs for Windows and Linux as well.

Use this walkthrough as a guide till you are more comfortable with these steps and start to customize these instructions to your likings. 

This is a somewhat barebones setup but this will work very well with what you will be doing at Lambda School.

## I will show you how to:
- How to <a href="https://brew.sh/">HomeBrew</a>

- How to Install <a href="https://git-scm.com/">Git</a>

- How to Install <a href="https://nodejs.org/en/">Node</a>  

- How to Install <a href="https://code.visualstudio.com/">VS Code</a>

## Install Homebrew
In this walkthrough I'll be using Homebrew for most of the main installs

Homebrew is a package manager much like NPM is for node and javascript.

As you will see here, homebrew makes it trivial to get a basic dev setup up and running.

To install brew, run the following command in your macOS terminal

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

And Viola, brew should now be installed

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

check node version

```
node --version
```

```
npm --version
```

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
- Duplicate Line      Alt + Shift + Down/Up Arrow
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