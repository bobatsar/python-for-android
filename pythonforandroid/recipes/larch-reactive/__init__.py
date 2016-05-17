import os
import sh
from os.path import join, dirname
from pythonforandroid.toolchain import shprint, info
from pythonforandroid.recipe import CompiledComponentsPythonRecipe
from pythonforandroid.util import ensure_dir


class LarchReactiveRecipe(CompiledComponentsPythonRecipe):
    name = 'larch-reactive'
    site_packages_name = 'larch/reactive'
    depends = [('python2', 'python3crystax')]
    patches = ['core.patch']

    def get_recipe_env(self, arch):
        env = super(LarchReactiveRecipe, self).get_recipe_env(arch)
        ndk = self.ctx.ndk_dir

        include = (
            " -I{ndk}/sources/cxx-stl/gnu-libstdc++/{version}/include/"
            " -I{ndk}/sources/cxx-stl/gnu-libstdc++/{version}/libs/"
            "{arch}/include")
        include = include.format(ndk=self.ctx.ndk_dir,
                                 version=env["TOOLCHAIN_VERSION"],
                                 arch=arch.arch)
        env["CC"] += include

        lib = "{ndk}/sources/cxx-stl/gnu-libstdc++/{version}/libs/{arch}"
        lib = lib.format(ndk=self.ctx.ndk_dir,
                         version=env["TOOLCHAIN_VERSION"],
                         arch=arch.arch)
        env["LDFLAGS"] += " -lgnustl_shared -L"+lib
        return env

    def prepare_build_dir(self, arch):
        home = os.environ["LARCH_HOME"]
        build_dir = self.get_build_dir(arch)
        shprint(sh.rm, '-rf', build_dir)
        shprint(sh.cp, '-r', join(home, "reactive"), build_dir)

    def build_arch(self, arch, *extra_args):
        super(LarchReactiveRecipe, self).build_arch(arch, *extra_args)

        # copy stl library
        ndk = self.ctx.ndk_dir
        env = self.get_recipe_env(arch)

        lib = "{ndk}/sources/cxx-stl/gnu-libstdc++/{version}/libs/{arch}"
        lib = lib.format(ndk=self.ctx.ndk_dir,
                         version=env["TOOLCHAIN_VERSION"],
                         arch=arch.arch)
        stl_lib = join(lib, "libgnustl_shared.so")

        dst_dir = join(self.ctx.get_python_install_dir(), "lib")
        ensure_dir(dst_dir)
        shprint(sh.cp, stl_lib, dst_dir)

recipe = LarchReactiveRecipe()
