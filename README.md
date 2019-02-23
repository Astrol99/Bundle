# Bundle
A discord bot that let's you install external cogs through a single command

![Example of bundle bot](https://github.com/Astrol99/Bundle/blob/master/resources/Capture1.PNG)

## Installation
**WARNING**: Some parts tested on Windows 10 and others on macOS Mojave since I work on both machines

#### 0. Install necessary packages and programs
- Python3 (recommended to be 3.6.6)

[Python3.6](https://www.python.org/downloads/release/python-366/)
- git

[Official git website](https://git-scm.com/)

- discord 1.0.0a rewrite
```
pip3 install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]
```
#### 1. Install files
```
git clone https://github.com/Astrol99/Bundle.git
```
#### 2. Make token file
Make a .txt file named "token" and insert your bot token on the first line.
#### 3. Run bot 
```
python bot.py
```
That's it!
~~Unless you get errors~~

## Usage

**NOTE**: The install and uninstall commands are hidden and cannot be used from users that don't have admin permissions in your server in order to protect abuse and spam.
### Installing other cogs

In order to install other cogs, you must use a git repo where the repo name and cog file name are the same.
Usage:
```
./install <github repository link>
```
Example:
In discord, when your bot is online,
```
./install https://github.com/Astrol99/Slanted.git
```
And then the bot will automatically reload it for you and will be ready to use!
### Uninstalling cogs
You can easily name the cogs by doing:
```
./list_cogs
```
and it will show a list of all cogs in the cog folder.
All cogs are named: "cogs.<cog_name>"
Usage:
```
./uninstall cogs.<cog_name>
```
You will need this to uninstall cogs. For example:
```
./uninstall cogs.test
```