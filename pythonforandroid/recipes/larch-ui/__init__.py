import sh
import os
from os.path import join
from pythonforandroid.toolchain import shprint, info
from pythonforandroid.recipe import PythonRecipe
from pythonforandroid.util import current_directory


class LarchUIRecipe(PythonRecipe):
    name = 'larch-ui'
    site_packages_name = 'larch/ui'
    depends = ['python2', "webviewjni", "pyjnius", "setuptools",
               'larch-reactive', "pyicu", "gevent", "msgpack-python",
               "cdecimal", "wsaccel", "ujson", "larch-aspect"]
    python_depends = ['werkzeug', "gevent-websocket"]

    call_hostpython_via_targetpython = False
    install_in_hostpython = False

    def prepare_build_dir(self, arch):
        home = os.environ["LARCH_HOME"]
        build_dir = self.get_build_dir(arch)
        shprint(sh.rm, '-rf', build_dir)
        shprint(sh.cp, '-r', join(home, "ui"), self.get_build_dir(arch))

        info("remove development files")
        src_dir = join(build_dir, "larch", "ui")
        with current_directory(src_dir):
            shprint(sh.rm, '-rf', "css")
            shprint(sh.rm, '-rf', "js")

        not_needed = ("js", "coffee", "scss", "css", "jar")
        to_remove = [
            join(path, f)
            for path, _, files in os.walk(src_dir)
            for f in files if f.rsplit(".", 1)[-1] in not_needed]

        for p in to_remove:
            shprint(sh.rm, p)

recipe = LarchUIRecipe()
