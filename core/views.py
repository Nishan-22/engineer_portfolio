from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django_ratelimit.decorators import ratelimit
from .models import Profile, Skill, Experience, Education, Certificate
from .forms import ContactForm
from projects.models import Project
import os


def home(request):
    profile = Profile.objects.first()
    try:
        from blog.models import Post
        latest_posts = Post.objects.filter(status='published')[:2]
    except Exception:
        latest_posts = []

    context = {
        'profile': profile,
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
        'education': Education.objects.all(),
        'certificates': Certificate.objects.all(),
        'latest_posts': latest_posts,
    }

    return render(request, 'core/home.html', context)


def storage_debug(request):
    """
    Lightweight debug endpoint to verify storage config on Render.
    """
    return JsonResponse({
        "DEFAULT_FILE_STORAGE": settings.DEFAULT_FILE_STORAGE,
        "CLOUDINARY_URL_present": bool(os.getenv("CLOUDINARY_URL")),
    })


def image_debug(request):
    """
    Debug the actual stored values and storage class for the profile photo.
    """
    profile = Profile.objects.first()
    if not profile or not profile.photo:
        return JsonResponse({
            "has_profile": bool(profile),
            "has_photo": False,
        })

    storage = type(profile.photo.storage).__name__

    return JsonResponse({
        "has_profile": True,
        "has_photo": True,
        "photo_name": profile.photo.name,
        "photo_url": profile.photo.url,
        "storage_class": storage,
    })


@ratelimit(key='ip', rate='5/h', method='POST')
def contact(request):
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            full_message = f"Message from {name} ({email}):\n\n{message}"
            
            try:
                send_mail(
                    subject,
                    full_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [profile.email if profile else settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, "There was an error sending your message. Please try again later.")
            
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'core/contact.html', context)