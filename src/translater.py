import cherrypy


class Translator(object):

    @cherrypy.expose
    def ping(self):
        return 'OK'

    @cherrypy.expose
    def translate(self, text='nothing', src='de', dest='en'):
        # TODO High sophisticated translation needed
        return '%s_%s_%s' % (src, dest, text)


if __name__ == '__main__':
    # Global cherrypy config
    cherrypy.config.update(
        {'server.socket_host': '0.0.0.0',
         'server.socket_port': 8081,
         'log.access_file': 'cherrypi.access.log',
         'log.error_file': 'cherrypi.error.log',
         'tools.encode.on': True,
         'tools.encode.encoding': 'utf-8'})

    cherrypy.tree.mount(Translator(), '/')
    cherrypy.engine.start()
    cherrypy.engine.block()
