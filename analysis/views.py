# analysis/views.py
from django.shortcuts import render
from django.http import JsonResponse
import cv2
import numpy as np
from .form import ImageUploadForm

def process_image(image_path):
    img = cv2.imread(image_path)
    height, width, _ = img.shape
    square_height = height // 10
    
    colors = []
    for i in range(10):
        roi = img[i * square_height:(i + 1) * square_height, :]
        mean_color = cv2.mean(roi)[:3]
        rgb_color = [int(mean_color[2]), int(mean_color[1]), int(mean_color[0])]  # Convert to RGB
        colors.append(rgb_color)

    return {
        'URO': colors[0],
        'BIL': colors[1],
        'KET': colors[2],
        'BLD': colors[3],
        'PRO': colors[4],
        'NIT': colors[5],
        'LEU': colors[6],
        'GLU': colors[7],
        'SG': colors[8],
        'PH': colors[9],
    }

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            result = process_image(image_instance.image.path)
            return render(request, 'analysis/result.html', {'result': result})
    else:
        form = ImageUploadForm()
    return render(request, 'analysis/form.html', {'form': form})
