from pyexpat import model
from ocr_project.celery import app
from celery import shared_task
from . import models
from . import ocr
import pathlib

@shared_task(name='process_image')
def process_image(id, image_path):
    image : models.ImageData = models.ImageData.objects.get(pk=id)
    result = ocr.extract_data(image_path)
    image.text = str(result)
    image.status = 1
    image.save()
    print("finish and success")