# core/urls.py
from django.contrib import admin
from django.urls import path, include
# Here we have included authentication urls to the main django project
# All path starting with 'auth/' will be looked up in authentication app urls file
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('webapp.urls'))
]
