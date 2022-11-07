from celery import Celery, signature
import ocr
import json
import numpy as np

app = Celery('celery_app', broker='pyamqp://guest@127.0.0.1:5672')

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

@app.task(name='process_image_test')
def test(id):
    print("process image id " + str(id))

@app.task(name='process_image')
def process_image_task(id, image_path):
    result = ocr.extract_data(image_path)

    list_result = list()
    for item_result in result:
        list_result.append({
            "first_value" : item_result[0],
            "text" : item_result[1],
            "ratio" : item_result[2]
        })

    result_json = json.dumps(list_result, cls=NpEncoder)
    
    signature('process_result', args=(id, result_json)).delay()


if __name__ == '__main__':
    app.start()
