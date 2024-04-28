from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_page, name='text_page'),
]