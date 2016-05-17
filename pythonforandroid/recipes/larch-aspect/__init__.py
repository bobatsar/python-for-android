import sh
import os
from os.path import join
from pythonforandroid.toolchain import shprint, info
from pythonforandroid.recipe import PythonRecipe


class LarchAspectRecipe(PythonRecipe):
    name = 'larch-aspect'
    site_packages_name = 'larch/aspect'
    depends = [('python2', 'python3crystax'), "setuptools"]

    call_hostpython_via_targetpython = False
    install_in_hostpython = False

    def prepare_build_dir(self, arch):
        home = os.environ["LARCH_HOME"]
        build_dir = self.get_build_dir(arch)
        shprint(sh.rm, '-rf', build_dir)
        shprint(sh.cp, '-r', join(home, "aspect"), self.get_build_dir(arch))

recipe = LarchAspectRecipe()
