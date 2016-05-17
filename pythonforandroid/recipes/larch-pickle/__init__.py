import os
import sh
from pythonforandroid.recipe import CythonRecipe


class LarchPickleRecipe(CythonRecipe):
    version = '1.1.0'
    url = 'https://pypi.python.org/packages/source/l/larch-pickle-{version}.tar.gz'
    url = "https://pypi.python.org/packages/d6/f2/6ee3b818976559ed5cd2552faf4a1029381f6e1f0ba940b464061d41106c/larch-pickle-1.1.0.tar.gz"
    depends = [('python2', 'python3crystax')]


recipe = LarchPickleRecipe()
