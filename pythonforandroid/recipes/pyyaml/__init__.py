from pythonforandroid.toolchain import PythonRecipe


class PyYamlRecipe(PythonRecipe):
    # name = geventwebsocket
    url = 'https://pypi.python.org/packages/59/19/7279d8d457471334901978345b2c3729eeed3bad8bbcc981a8066480c66a/pyaml-15.8.2.tar.gz'
    depends = [('python2', 'python3crystax')]
    site_packages_name = 'yaml'

recipe = PyYamlRecipe()
