from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.HomePage, name='home-page'),
    url('stream/', views.Stream, name='stream'),
    url(r'^camera_on/', views.camera_on, name='camera_on'),
]
