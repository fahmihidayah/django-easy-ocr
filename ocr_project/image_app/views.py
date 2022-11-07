from django.shortcuts import render
from django_tables2 import SingleTableView
from django.views import generic
from . import tables
from . import models
from . import forms
from . import tasks
from celery import signature
from django.urls import reverse, reverse_lazy
# Create your views here.

# class ImageDataSingleTableView(SingleTableView):


class ImageDataSingleTableView(SingleTableView):
    template_name = 'image_app/list_image_app.html'
    table_class = tables.ImageDataTable
    paginate_by = 10
    model = models.ImageData


class ImageDataCreateView(generic.CreateView):
    template_name = 'image_app/form_image_app.html'
    model = models.ImageData
    form_class = forms.ImageDataForm
    success_url = reverse_lazy('view_images')
    
    def form_valid(self, form):
        self.object = form.save()
        signature('process_image_test', args=(self.object.pk,),).delay()
        # tasks.process_image.delay(self.object.pk)
        return super().form_valid(form)

class ImageDataDetailView(generic.TemplateView):
    template_name = 'image_app/form_image_app.html'