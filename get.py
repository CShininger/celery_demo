from celery_task.celery import app


from celery.result import AsyncResult

id_id='c9c65d81-a04d-48f8-912c-ad488882bb21'

if __name__=='__main__':
    result=AsyncResult(id_id,app=app)
    if result.successful():
        result=result.get()
        print(result)
    elif result.failed():
        print('fault')
    elif result.status =='PENDING':
        print('pending')
