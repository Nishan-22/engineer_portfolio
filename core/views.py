from django.shortcuts import render
from .models import Profile, Skill, Education, Certificate
from projects.models import Project


def home(request):
    context = {
        'profile': Profile.objects.first(),
        'technical_skills': Skill.objects.filter(category='technical'),
        'field_skills': Skill.objects.filter(category='field'),
        'projects': Project.objects.all(),
        'education': Education.objects.all(),
        'certificates': Certificate.objects.all(),
    }

    return render(request, 'core/home.html', context)