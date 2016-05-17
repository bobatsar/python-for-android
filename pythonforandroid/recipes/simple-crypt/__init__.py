from pythonforandroid.toolchain import PythonRecipe


class SimpleCryptRecipe(PythonRecipe):
    # name = geventwebsocket
    url = 'https://pypi.python.org/packages/60/66/5bf6feb073f715a61492f8a6d444ad3d884ada71af317ce7a9c80bebee60/simple-crypt-4.1.7.tar.gz'
    depends = [('python2', 'python3crystax'), 'pycrypto']
    site_packages_name = 'simplecrypt'

recipe = SimpleCryptRecipe()
