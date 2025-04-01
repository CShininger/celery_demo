import time

from .celery import   app

@app.task
def send_email(to='asd'):
    print('邮件发送start%s发 email'%to)
    time.sleep(2)
    print('邮件发送end')
    return '向%s发送end' % to
