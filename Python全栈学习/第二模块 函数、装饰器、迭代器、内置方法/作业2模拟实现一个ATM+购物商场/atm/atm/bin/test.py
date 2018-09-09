#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/4 13:24

import datetime

from dateutil.relativedelta import relativedelta

expire_date = str(datetime.datetime.today() + relativedelta(years=+5))
print(expire_date[:10])