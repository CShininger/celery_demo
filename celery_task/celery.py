from celery import  Celery
# broker redis 消息中间件
broker='redis://127.0.0.1:6379/1'


# backend redis 数据存储
backend='redis://127.0.0.1:6379/2'

# 实例化app对象
app= Celery('demo',broker=broker,backend=backend,
            include=[
                'celery_task.crawl_task',
                'celery_task.user_task',
            ])

app.conf.timezone='Asia/Shanghai'

app.conf.enable_utcnow=False

from datetime import timedelta

app.conf.beat_schedule = {
    'low-task':{
        'task':'celery_task.user_task.send_email',
        'schedule':timedelta(seconds=5),
        'args':(),
    }
}