from django.shortcuts import render,redirect

# Create your views here.

from auth_app.forms import *
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})


from django.contrib.auth import authenticate, login as auth_login
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            context = {
                'error_message': 'Username or Password is incorrect!',
            }
            return render(request, 'user_app/login.html', context)
    return render(request, 'login.html')

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('/') 



def profileupdate(request):

    if request.method == 'POST':
        u_form = UserUpdate(request.POST,instance=request.user)
        p_form = ProfileUpdet(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request, 'Profile details updated.')
            return redirect('profile-page')

    else:
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdet(instance=request.user.profile)       

    context={
        'u_form':u_form,
        'p_form':p_form,
    }     
    return render(request,'profileupdate.html',context)


def profile(request):
    return render(request,'profile.html')  