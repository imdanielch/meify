#!/usr/bin/env python3
'''Automate copying over config files'''

import subprocess
from distutils.dir_util import copy_tree
from distutils.dir_util import log 

log.set_verbosity(log.INFO)
log.set_threshold(log.INFO)
copy_tree("./cfgfiles", "~/")


# Install vim Vundle and their plugins.
subprocess.call(["vim", "+PluginInstall", "+qall"])
