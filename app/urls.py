from django.urls import path
from . import views

urlpatterns = [
    path('', views.pdf_to_img, name='pdf_to_img'),
    path('/<path:image_url>/', views.preview_image, name='preview_image'),
    path('download-images/', views.download_images, name='download_images'),
]
