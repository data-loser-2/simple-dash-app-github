# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


# @scheduler.scheduled_job('interval', seconds=3)
# def timed_job():
#     print('This job is run every three seconds.')


@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')


scheduler.start()
