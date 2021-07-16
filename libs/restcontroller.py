import importlib

from libs.apicontroller import ApiController
from libs.kit import Kit


class RestController(ApiController):
    name = None

    def prepare(self):
        super().prepare()
        clazz_name = Kit.capitalize(self.name)
        imp = importlib.import_module('models.%s' % self.name)
        self.clazz = getattr(imp, clazz_name)

    def get_list(self):
        if not self.name:
            return
        data = self.clazz.get_all()
        self.make_pager_result(data)

    def post_save(self):
        pdata = self.get_data()
        site = self.clazz.save_from_data(pdata)
        self.make_pager_result(site)

    def get_info(self):
        pdata = self.validate(['id'])
        find = self.clazz.get_one_or_none(self.clazz.id == pdata['id'])
        self.make_result(find)

    def post_delete(self):
        pdata = self.validate(['id'])
        self.clazz.delete_with(self.clazz.id == pdata['id'])
        self.make_msg('删除成功')
