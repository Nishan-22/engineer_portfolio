from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage


class Category(models.Model):
    name = models.CharField(max_length=100)  # e.g. Building, Bridge, Road

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    location = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)  # e.g. "2022–2023"
    role = models.CharField(max_length=200)  # e.g. Site Engineer

    tools_used = models.CharField(max_length=200, blank=True)  # AutoCAD, ETABS

    image = models.ImageField(upload_to='projects/', storage=MediaCloudinaryStorage())
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title