from . import models
from django import forms


class ImageDataForm(forms.ModelForm):

    class Meta:
        model = models.ImageData
        fields = ['title', 'image',]