import importlib
import inspect
import logging


from libs.aiapplication import AiApplication


class BaseTask:
    ctx = None
    params = []

    def __init__(self):
        # self.__init_logging()
        self.ctx = self.application = AiApplication(None)
        if self.ctx.cfg.postgres and not self.ctx.cfg.postgres.enabled:
            DbHandler = importlib.import_module('handlers.dbhandler', 'DbHandler')
            DbHandler.refresh_proxy(self.ctx.cfg.postgres)

    def __init_logging(self):
        logging.basicConfig(
            filename='aitask.log',
            level=logging.DEBUG,
            format='[%(asctime)s] %(levelname)s  {%(filename)s:%(lineno)d} - %(message)s',
            datefmt='%H:%M:%S',
        )

        logging.getLogger('requests').setLevel(logging.ERROR)
        logging.getLogger('connectionpool').setLevel(logging.ERROR)
        logging.getLogger('peewee').setLevel(logging.ERROR)
        logging.getLogger('tornado.access').setLevel(logging.ERROR)
        logging.getLogger('asyncio').setLevel(logging.ERROR)
        logging.getLogger('elasticsearch').setLevel(logging.ERROR)
        logging.getLogger('urllib3.connectionpool').setLevel(logging.ERROR)

        stderrLogger = logging.StreamHandler()
        stderrLogger.setFormatter(
            logging.Formatter('[%(name)s] %(asctime)s] %(levelname)s  {%(filename)-16s:%(lineno)d} - %(message)s'))
        logging.getLogger().addHandler(stderrLogger)

    def init(self):
        pass

    def set_params(self, params):
        self.params = params

    def get_param(self, index):
        if index >= len(self.params):
            return None
        else:
            return self.params[index]

    def run(self):
        for x in inspect.getmembers(self):
            method_name = x[0]
            if 'task_' in method_name:
                method = getattr(self, method_name)
                method()
