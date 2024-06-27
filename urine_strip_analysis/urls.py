# urine_strip_analysis/urls.py
from django.contrib import admin
from django.urls import path
from analysis import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('admin/', admin.site.urls),
]
