from django.contrib import admin
from . import models, forms
# Register your models here.


@admin.register(models.ImageData)
class ImageDataModelAdmin(admin.ModelAdmin):
    search_fields = ['title', 'image', 'status']
    list_display = ['title', 'image', 'status', 'created_at', 'updated_at']
    form = forms.ImageDataForm
