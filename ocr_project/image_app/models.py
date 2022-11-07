from django.db import models

# Create your models here.


class ImageData(models.Model):

    title: models.CharField = models.CharField(max_length=150)

    image: models.ImageField = models.ImageField(upload_to='images/')

    text: models.TextField = models.TextField(max_length=2000, default='', null=True)

    status: models.IntegerField = models.IntegerField(default=0)

    clean_text: models.TextField = models.TextField(max_length=5000, default='', null=True)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True, editable=False)

    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title
