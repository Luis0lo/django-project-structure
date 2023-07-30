from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),#include all the urls in base app
]

'''
    create an admin user to access /admin
    
    python manage.py createsuperuser (test, test, test@gmail.com)

    you'll need to set in base/admin file the room to be seen in admin
'''
