# authentication/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from webapp.models import Student, Teacher, User

class CustomUserCreationForm(UserCreationForm):
    fullname = forms.CharField(max_length=100, required=True)
    student_number = forms.CharField(max_length=20, required=True)
    sex = forms.CharField(max_length=1, required=True)
    contact_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'fullname', 'student_number', 'sex', 'contact_number')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)

class TeacherCreationForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ('email',)

class TeacherChangeForm(UserChangeForm):
    class Meta:
        model = Teacher
        fields = ('email',)

class StudentCreationForm(UserCreationForm):
    fullname = forms.CharField(max_length=100, required=True)
    student_number = forms.CharField(max_length=20, required=True)
    sex = forms.CharField(max_length=1, required=True)
    contact_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'fullname', 'student_number', 'sex', 'contact_number')

class StudentChangeForm(UserChangeForm):
    class Meta:
        model = Student
        fields = ('email',)
