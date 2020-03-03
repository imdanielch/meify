"""
collect all relevant config files
"""
import distutils
from distutils import dir_util
import shutil
import os

print "copy recursively " + os.path.join(os.path.expanduser("~"), ".zsh")
print "to " + os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cfgfiles', '.zsh')
distutils.dir_util.copy_tree(os.path.join(os.path.expanduser("~"), ".zsh"), os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cfgfiles', '.zsh'));
print ""

print "copy " + os.path.join(os.path.expanduser("~"), ".zshrc")
print "to " + os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cfgfiles')
shutil.copy(os.path.join(os.path.expanduser("~"), ".zshrc"), os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cfgfiles'));
print ""

print "copy " + os.path.join(os.path.expanduser("~"), ".vimrc")
print "to " + os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cfgfiles')
shutil.copy(os.path.join(os.path.expanduser("~"), ".vimrc"), os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cfgfiles'));
print ""
