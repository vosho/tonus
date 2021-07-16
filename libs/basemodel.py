import json

from peewee import Model
from playhouse.shortcuts import model_to_dict

from libs.kit import Kit


class BaseModel(Model):
    @classmethod
    def get_one_or_none(cls, *query, **kwargs):
        finds = cls.select().where(*query)
        if finds.count():
            return finds[0]
        return None

    @classmethod
    def get_all(cls, *query, **kwargs):
        if query:
            finds = cls.select().where(*query)
        else:
            finds = cls.select()
        if 'order' in kwargs:
            finds = finds.order_by(kwargs['order'])

        if finds.count():
            return finds
        else:
            return []

    def to_json(self):
        return model_to_dict(self)

    def __str__(self):
        return json.dumps(self.to_json(), indent=4)

    @classmethod
    def delete_with(cls, where):
        q = cls.delete().where(where)
        q.execute()

    @classmethod
    def save_from_data(cls, data, id='id', only=[]):
        if 'id' in data:
            find = cls.get_or_none(cls.id == data[id])
            if find:
                # update
                for k in find.__data__:
                    if k in data:
                        setattr(find, k, data[k])
                    if k == 'utime':
                        now = Kit.datetime_now(['-', ' ', ':'])
                        setattr(find, k, now)
                print(find)
                if len(only):
                    find.save(only=only)
                else:
                    find.save()
                return find

        param = {
            'name': '123123123123'
        }
        for k in cls.__dict__:
            if k[0] != '_' and k in data:
                param[k] = data[k]
            if k == 'ctime':
                now = Kit.datetime_now(['-', ' ', ':'])
                param[k] = now
            if k == 'utime':
                now = Kit.datetime_now(['-', ' ', ':'])
                param[k] = now
        return cls.create(**param)
