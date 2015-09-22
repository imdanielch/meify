#!/usr/bin/env python3
'''Automate copying over config files'''

import subprocess
from os.path import expanduser
from os.path import exists
from distutils.dir_util import copy_tree
from distutils.dir_util import log 

home = expanduser("~")
log.set_verbosity(log.INFO)
log.set_threshold(log.INFO)
copy_tree("./cfgfiles", home)

if exists(home + "/.vim/bundle/Vundle.vim") != True:
    print("Installing Vundle.")
    subprocess.call(["git", "clone", "https://github.com/VundleVim/Vundle.vim.git", home + "/.vim/bundle/Vundle.vim"])
# Install vim Vundle and their plugins.
print("Vundle installed, update vim plugins")
subprocess.call(["vim", "+PluginInstall", "+qall"])
print("Meify finished running, please restart your terminal.")
