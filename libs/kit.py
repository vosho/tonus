import math
import re

import moment
from datetime import datetime, date, timedelta


class Kit:
    @staticmethod
    def get_dir():
        pass

    @staticmethod
    def date_now(diff=0):
        return moment.now().add(days=diff).format('YYYY-MM-DD')
    @staticmethod
    def timestamp():
        return math.floor(datetime.now().timestamp() * 1000)

    @staticmethod
    def now(diff=0):
        return moment.now()

    @staticmethod
    def week_now(diff=0):
        week = moment.now().add(weeks=diff).date.isocalendar()[1]
        return '%s%02d' % (Kit.year_now(), week)

    @staticmethod
    def month_now(diff=0):
        if diff == 0:
            return moment.now().add(months=diff).format('YYYYMM')
        else:
            today = date.today()
            lastMonth = today - timedelta(months=1)
            print('-----' + lastMonth.strftime("%Y%m"))

    @staticmethod
    def day_now(diff=0, format='YYYYMMDD'):
        return moment.now().add(days=diff).format(format)

    @staticmethod
    def hour_now(diff=0, format='YYYYMMDDHH'):
        return moment.now().add(hours=diff).format(format)

    @staticmethod
    def minute_now(diff=0):
        return moment.now().add(hours=diff).format('YYYYMMDDHH')

    @staticmethod
    def year_now():
        now = datetime.now()
        return now.strftime('%Y')

    @staticmethod
    def datetime_now(seps=None):
        if seps is None:
            seps = ['', '', '']
        now = datetime.now()
        sep0 = seps[0]
        sep1 = seps[1]
        sep2 = seps[2]
        return now.strftime('%Y' + sep0 + '%m' + sep0 + '%d' + sep1 + '%H' + sep2 + '%M' + sep2 + '%S')

    @staticmethod
    def capitalize(s):
        def c(x):
            x = x.group(0)
            x = x.replace('_', '')
            x = x.replace('-', '')
            x = x.upper()
            return x

        return re.sub(r'([_|\-][a-z]|^[a-z])', c, s)

if __name__ == '__main__':
    print(Kit.month_now(-1))
    print(Kit.month_now(0))
    print(Kit.date_now(-1))
