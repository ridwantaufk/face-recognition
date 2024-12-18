from django.urls import path
from . import views

urlpatterns = [
    path('webcam/', views.webcam_view, name='webcam_view'),  # Halaman utama untuk webcam webcam
]
