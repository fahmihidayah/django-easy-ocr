from celery import Celery, signature, shared_task

app = Celery('project', broker='pyamqp://guest@127.0.0.1:5672')

@app.task(name='process_result')
def process_result(id, result_json):
    print("id image is " + str(id))
    print(result_json)

if __name__ == '__main__':
    app.start()