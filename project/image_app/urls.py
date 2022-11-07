from django.urls import path
from . import views

urlpatterns = [
    path('images', views.ImageDataSingleTableView.as_view(), name='view_images'),
    path('images/create', views.ImageDataCreateView.as_view(), name='view_create_images'),
    path('images/<int:pk>', views.ImageDataDetailView.as_view(), name='view_detail_images'),
]