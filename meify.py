#!/usr/bin/env python3
'''Automate copying over config files'''

import subprocess
from os import chdir
from os.path import expanduser
from os.path import exists
from distutils.dir_util import copy_tree
from distutils.dir_util import log

home = expanduser("~")
print("Home directory set as :" + home)
log.set_verbosity(log.INFO)
log.set_threshold(log.INFO)
copy_tree("./cfgfiles", home)

if not exists(home + "/.nvm"):
    print("Installing nvm")
    subprocess.call([
        "curl",
        "-o-",
        "https://raw.githubusercontent.com/creationix/nvm/v0.29.0/install.sh", "|", "bash"])

if not exists(home + "/.vim/bundle/Vundle.vim/README.md"):
    print("Installing Vundle.")
    subprocess.call([
        "git",
        "clone",
        "https://github.com/VundleVim/Vundle.vim.git", home + "/.vim/bundle/Vundle.vim"])

# Install vim Vundle and their plugins.
print("Vundle installed, update vim plugins")
subprocess.call(["vim", "+PluginInstall", "+qall"])
# install powerline fonts
chdir("..")
subprocess.run("git clone https://github.com/powerline/fonts.git", shell=True)
subprocess.run("sh fonts/.install.sh", shell=True)

print("Meify finished running, please restart your terminal.")
