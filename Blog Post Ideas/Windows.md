# Initial Development Setup for Windows

I am going to show you a very basic initial setup of your development environment for Lambda School.

This tutorial will focus mainly on VS Code and Windows 10. I will have other guides and walkthroughs for Mac OSX and Linux as well.

Use this walkthrough as a guide till you are more comfortable with these steps and start to customize these instructions to your likings. 

This is a somewhat barebones setup but this will work very well with what you will be doing at Lambda School.

## I will show you how to:
- How to Install WSL

- How to Install <a href="https://git-scm.com/">Git</a>

- How to Install <a href="https://nodejs.org/en/">Node</a>  

- How to Install <a href="https://code.visualstudio.com/">VS Code</a>

## Install WSL
The first thing we will do Is setup and install WSL.

> WSL is Windows Subsystem for Linux and is a BASH alternative. 

Instead of using Git Bash or your command prompt I will show you how I go through and set up WSL as painless as possible.

I will show the steps to install git, node and everything needed inside WSL.

### Turning on WSL Windows Feature
Before going into the Windows Store and picking out our Linux Distribution

We need to turn on the WSL feature for it.

To do that we have just a few steps to take.

### Option 1:
> Tap your Windows Button, and start typing `turn windows features on or off`

> Hit enter and it should bring up a list that looks like:

  IMAGE HERE

> Scroll down and find the feature labeled `Windows Subsystem for Linux` and mark that box as checked.

> Click ok and let it install and restart your computer when asked.

### Option 2:
> Open PowerShell as Administrator and run

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

> Restart when prompted

Now we will go ahead and open up the Windows Store and search `Linux`

For this video I will be choosing Ubuntu, once it is installed we will go through the initial setup.

### Initialize the Distro
Now that is is installed, go ahead and launch whichever distro you chose.

The First time it is ran, a Console window will open and you will be asked to wait for a few minutes for the installation to complete.

Once installation is complete, you will be prompted to create a new user account.

Once you have created your account, now all that is left to do is run the following command

```
sudo apt update && sudo apt upgrade
```

You will be asked for your password and Linux will start the update and upgrade process.

Congrats! WSL is now installed, we will go through installing git and node at those sections.

## Installing Git
First things first lets go download git from <a href="https://git-scm.com/">Git</a>.

<img src="" alt="img" />
<img src="" alt="img" />
<img src="" alt="img" />
<img src="" alt="img" />

If you're using Mintty for your console, you should be able to run:

```
git --version
```

Now you should see your version and be good to go. 

BUT if you're on linux and get the error saying git is not installed

Run the following command to install git

```
sudo apt install git
```

***

### Initial Git Setup

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


### Sharing an existing SSH key
If you have an SSH key already setup on Windows you could reuse it rather than creating a new one. (Note that PuTTY keys do not work here). To do this you can just copy the key from the Windows filesystem into the WSL’s filesystem. Linux has some rules about how visible the key is. So you need to make sure the access levels are strict enough to meet these requirements:

run these commands as follows one at a time:
- cd ~
- mkdir .ssh
- chmod 700 .ssh
- cd .ssh
- cp /mnt/c/Users/user/.ssh/id_rsa* .
- chmod 600 id_rsa
- chmod 644 id_rsa.pub

Now you should be able to go to github and try pulling down a repo as ssh.

## Installing Node
First things first if go and install <a href="https://nodejs.org/en/">Node</a>

I typically download the most current version but the LTS version is perfectly fine.

Once downloaded and installed close your terminal and reopen.
Then run the following commands:

```
node --version
npm --version
```

Now if you're using Mintty you are probably good to go, WSL may be saying there is no node installed or it's an old version, so lets fix that.

First things first, lets run update and upgrade

```
sudo apt update && sudo apt upgrade
```

I am probably going to do this way differently than you have seen before. 
I will be installing Homebrew for Linux and we will install node that way. 
In my opinion that has been the easiest way for WSL to have the most up to date version of node.

### Homebrew for Linux
So for right now, lets visit this site <a href="https://docs.brew.sh/Homebrew-on-Linux">Homebrew</a>

and just to be save, lets install some build-essential tools
```
sudo apt-get install build-essential curl file git
```

Read through the documentation and learn a little bit about what homebrew does and what it is useful for.

now essentially there are 5 commands we will be running.
- `sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"`

- `test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)`

- `test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)`

- `test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile`

- `echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile`

One by one, run those commands

now lets install node

`brew install node`

and thats it. Run `node --version` and `npm --version` and you should be good to go.

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