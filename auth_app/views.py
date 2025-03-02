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
            return redirect('login_page')
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
            return render(request, 'login.html', context)
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


from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from core.settings import DEFAULT_FROM_EMAIL
from core import settings


# password reset
def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = reverse('reset_password_confirm', args=(uid, token))
            current_site = get_current_site(request)
            domain = current_site.domain

            mail_subject = 'Password Reset Request'

            message = render_to_string('reset-password-template.html', {
                'user': user,
                'domain': domain,
                'reset_link': reset_link,
            })

            send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)
            return render(request, 'reset-password-done.html', {'email': email})
        else:
            return render(request, 'reset-password.html', {'error_message': 'Email not found'})
    return render(request, 'reset-password.html')