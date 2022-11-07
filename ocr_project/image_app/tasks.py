from pyexpat import model
from ocr_project.celery import app
from celery import shared_task
from . import models
from . import ocr
import pathlib

def get_clearn_text(result):
    clean_text = ''
    for item_result in result:
        clean_text += item_result[1] + ' '
    return clean_text

@shared_task(name='process_image')
def process_image(id, image_path):
    image : models.ImageData = models.ImageData.objects.get(pk=id)
    result = ocr.extract_data(image_path)
    image.text = str(result)
    image.status = 1
    image.clean_text = get_clearn_text(result=result)
    image.save()
    print("finish and success")