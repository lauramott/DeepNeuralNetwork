# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
from django.core.files.base import ContentFile


class Stream(models.Model):
    image = models.ImageField


class PhotoModel(models.Model):
    video = models.FileField(upload_to='catalog/static/images')

    def save_file(request):
        photomodel = PhotoModel.objects.get(id=1)
        file_content = ContentFile(request.FILES['video'].read())
        photomodel.video.save(request.FILES['video'].name, file_content)
