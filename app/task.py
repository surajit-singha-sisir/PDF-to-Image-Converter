# tasks.py

from datetime import datetime
from celery import shared_task
from django.core.files.storage import FileSystemStorage
from pdf2image import convert_from_path

@shared_task
def convert_pdf(pdf_file_path):
    # Convert the PDF file to images using pdf2image package
    pages = convert_from_path(pdf_file_path)
    # Save each page of the PDF file as a separate image in the media folder
    image_paths = []
    for i, page in enumerate(pages):
        image_name = f'page_{i}.jpg'
        fs = FileSystemStorage()
        image_path = fs.save(image_name, page, max_length=None)
        image_url = fs.url(image_path)
        image_paths.append(image_url)
    # Return the list of image paths
    return image_paths
