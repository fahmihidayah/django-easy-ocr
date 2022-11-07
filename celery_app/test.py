from celery import signature


def call_task():
    signature("process_image_test", args=(123,)).delay()

if __name__ == '__main__':
    call_task()