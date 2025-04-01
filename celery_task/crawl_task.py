import time
from .celery import   app

@app.task
def crawl_email(to='asd'):
    print('爬虫%s发 email'%to)
    time.sleep(2)
    print('爬虫end')
    return '爬虫%s爬虫end' % to
