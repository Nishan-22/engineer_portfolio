from django.urls import path
from .views import home, contact, storage_debug

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
     path('storage-debug/', storage_debug, name='storage_debug'),
]