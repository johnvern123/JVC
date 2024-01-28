# authentication/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .views import profile
# path( "path string/", views.function, name="optional name of path"
urlpatterns = [
    path ('',views.homepage,name="homepage"),
    path ('login/',views.loginUser,name="login"),
    path ('logout/',views.logoutUser,name="logout"),
    path ('register-student/',views.registerStudent,name="register-student"),
    path ('register-teacher/',views.registerTeacher,name="register-teacher"),
    path ('profile/', profile, name='profile'),
    path ('about/', views.about, name="about.html"),
    path ('contact/', views.contact, name="contact.html"),
    path ('dashboard/', views.dashboard, name="dashboard.html"),
    path ('personnel/', views.personnel, name="personnel.html"),
    path ('favbook/', views.favbook, name="favbook.html"),
    path ('description1/', views.description1, name="description1.html"),
    path ('description2/', views.description2, name="description2.html"),
    path ('description3/', views.description3, name="description3.html"),
    path ('description4/', views.description4, name="description4.html"),
    path ('description5/', views.description5, name="description5.html"),
    path ('description6/', views.description6, name="description6.html"),
]
