from project.celery import app


@app.task(name='update_image')
def update_image(id, json_result):
    print(json_result)
    print(id)