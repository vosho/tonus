from libs.restcontroller import RestController


class HeartbeatController(RestController):
    def get_index(self):
        self.make_result({
            "msg": 'msg from api'
        })