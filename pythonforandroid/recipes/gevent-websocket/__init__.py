from pythonforandroid.toolchain import PythonRecipe


class GeventWebsocketRecipe(PythonRecipe):
    # name = geventwebsocket
    url = 'https://pypi.python.org/packages/de/93/6bc86ddd65435a56a2f2ea7cc908d92fea894fc08e364156656e71cc1435/gevent-websocket-0.9.5.tar.gz'
    depends = [('python2', 'python3crystax')]
    site_packages_name = 'geventwebsocket'

recipe = GeventWebsocketRecipe()
