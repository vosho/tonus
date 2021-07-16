from libs.restcontroller import RestController


class DemoController(RestController):
    def post_task(self):
        self.ctx.start_task('test')
        self.make_result({})
