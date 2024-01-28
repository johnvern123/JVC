# authentication/views.py
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from webapp.forms import StudentCreationForm, TeacherCreationForm
from .forms import CustomUserCreationForm, StudentCreationForm
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, "authentication/base.html")


def registerStudent(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})


def registerTeacher(request):
    if request.method=='POST':
        form = TeacherCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registered Successfully')
        else:
            messages.error(request,'Please recheck the form data')
        return redirect('register-teacher')
    form = TeacherCreationForm()
    title = "Teacher Registration"
    return render(request, 'authentication/register.html', {'form': form,'title':title})


def loginUser(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in Successfully")
            return redirect('homepage')
        else:
            messages.error(request,"Invalid credentials!")
    return render(request,'authentication/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'authentication/profile.html', {'user': request.user})


def about(request):
    return render(request, 'authentication/about.html')

def contact(request):
    return render(request, 'authentication/contact.html')

def dashboard(request):
    return render(request, 'authentication/dashboard.html')

def personnel(request):
    return render(request, 'authentication/personnel.html')

def favbook(request):
    return render(request, 'authentication/favbook.html')

def description1(request):
    return render(request, 'authentication/description1.html')

def description2(request):
    return render(request, 'authentication/description2.html')

def description3(request):
    return render(request, 'authentication/description3.html')

def description4(request):
    return render(request, 'authentication/description4.html')

def description5(request):
    return render(request, 'authentication/description5.html')

def description6(request):
    return render(request, 'authentication/description6.html')