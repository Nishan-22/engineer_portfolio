from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)  # Civil Engineer, Site Engineer etc.
    photo = models.ImageField(upload_to='profile/')
    about = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

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


class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=100, default='Full-time')
    start_date = models.CharField(max_length=100)  # e.g., "Mar 2024"
    end_date = models.CharField(max_length=100, default='Present')
    description = models.TextField(blank=True, null=True)
    key_projects = models.TextField(blank=True, null=True)
    skills_used = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=100)  # e.g., "2015 - 2019"

    def __str__(self):
        return self.degree


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    issue_date = models.CharField(max_length=100, default='N/A')
    expiration_date = models.CharField(max_length=100, blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title