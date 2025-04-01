# 这个用来提交任务
from celery_task.crawl_task import crawl_email
from datetime import datetime,timedelta

eta=datetime.utcnow()+timedelta(seconds=10)
res=crawl_email.apply_async(args=['aasd@qq.com'],eta=eta)
print(res)

# 同步
# res = add(7,8)
# print(res)

# 异步
# 向消息队列中提交了一个任务，计算7+8任务 但是没执行
# res= crawl_email.delay('测试1') # 没有延迟 直接返回
# print(res) # uuid 判断是否添加




# 使用命令 启动worker 执行被提交的任务 执行结束后 结果存储到redis
# celery_task 是包名
# win: celery -A celery_task worker -l info -P eventlet
# mac/linux: celery -A celery_task worker -l info

# celery -A celery_task beat -l info