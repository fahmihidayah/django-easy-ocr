from . import models
from django_tables2 import Table


class ImageDataTable(Table):

    class Meta:
        attrs = {"class": "table table-bordered"}
        model = models.ImageData
        template_name = "django_tables2/bootstrap4.html"
        fields = ['title', 'image', 'text', 'status', 'created_at', 'updated_at']
