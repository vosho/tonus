#-- encoding=utf-8 --
import logging
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from libs.aiapplication import AiApplication
from libs.logging import Logging


def main():
    Logging('server')
    prefix = 'api/v1/'
    app = AiApplication(prefix, 'config.json')
    http_server = HTTPServer(app)
    http_server.listen(app.cfg.server.port or 17002)
    logging.debug('Starting http server %d' % app.cfg.server.port)
    IOLoop.current().start()


if __name__ == '__main__':
    main()
