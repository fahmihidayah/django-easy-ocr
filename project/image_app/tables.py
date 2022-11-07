from . import models
from django_tables2 import Table, TemplateColumn


class ImageDataTable(Table):

    detail = TemplateColumn(template_name='image_app/table/detail.html')

    class Meta:
        attrs = {"class": "table table-bordered table-responsive"}
        model = models.ImageData
        template_name = "django_tables2/bootstrap4.html"
        fields = ['title', 'image', 'current_status', 'created_at', 'updated_at']
