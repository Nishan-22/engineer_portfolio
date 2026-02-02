from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)  # Civil Engineer, Site Engineer etc.
    photo = models.ImageField(upload_to='profile/')
    about = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('technical', 'Technical'),
        ('field', 'Field'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tools_used = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.degree
    
    
class Certificate(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    year = models.CharField(max_length=10)

    def __str__(self):
        return self.title