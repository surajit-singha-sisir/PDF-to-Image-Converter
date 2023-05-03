from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from pdf2image import convert_from_path
import os
import zipfile
from django.http import HttpResponse

def pdf_to_img(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        # Get the uploaded PDF file from request
        pdf_file = request.FILES['pdf_file']
        # Save the PDF file to the media folder
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)
        # Convert the PDF file to images using pdf2image package
        pages = convert_from_path(fs.path(filename))
        # Save each page of the PDF file as a separate image in the media folder
        image_paths = []
        for i, page in enumerate(pages):
            image_name = f'page_{i}.jpg'
            image_path = fs.path(image_name)
            page.save(image_path, 'JPEG')
            image_url = fs.url(image_path)
            image_paths.append(image_url)
        # Pass the list of image paths to the template for display
        context = {'image_paths': image_paths}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

def preview_image(request, image_url):
    return render(request, 'preview.html', {'image_url': image_url})

def download_images(request):
    # Get all image paths from the media folder
    fs = FileSystemStorage()
    image_paths = []
    for filename in os.listdir(fs.location):
        if filename.endswith('.jpg'):
            image_path = fs.path(filename)
            image_paths.append(image_path)
    # Create a zip file containing all images
    zip_filename = 'sisir-images.zip'
    zip_file_path = fs.path(zip_filename)
    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        for image_path in image_paths:
            zip_file.write(image_path, os.path.basename(image_path))
    # Download the zip file
    with open(zip_file_path, 'rb') as zip_file:
        response = HttpResponse(zip_file.read(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'
        return response
