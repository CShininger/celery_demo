import time

from celery import Celery

# broker redis 消息中间件
broker='redis://127.0.0.1:6379/1'


# backend redis 数据存储
backend='redis://127.0.0.1:6379/2'

# 实例化app对象
app= Celery('demo',broker=broker,backend=backend)


# 编写任务
@app.task # 被装饰器装饰之后算celery的任务
def add(a,b):
    print('a+b:',a+b)
    time.sleep(1) # 模拟耗时
    return a+b