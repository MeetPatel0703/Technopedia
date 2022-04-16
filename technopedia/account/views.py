from .models import TechUser
from django.shortcuts import render
from generic.views import *
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import auth, messages
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from .forms import Loginform
from django.views.generic.detail import DetailView


class Home(TemplateView):
    template_name = 'user/index.html'


class UserDetailView(DetailView):
    model = TechUser
    template_name = 'user/userdetail.html'
    context_object_name = 'user'


class MyLogin(LoginView):
    template_name = 'registration/login.html'
    authentication_form = Loginform


class MyLogout(LogoutView):
    template_name = 'user/index.html'


@method_decorator(login_required, name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'


def signuphandle(request):
    if request.method == 'POST':
        user_name = request.POST['uname']
        e_mail = request.POST['signupemail']
        password = request.POST['signuppass']
        c_password = request.POST['signupcpass']

        if TechUser.objects.filter(username=user_name).exists():
            messages.error(request, "This UserName Is Already Avalable.")
            return redirect("signup")
        if TechUser.objects.filter(email=e_mail).exists():
            messages.error(request, "User E-Mail Is Already Avalable.")
            return redirect("signup")
        if len(user_name) > 10:
            messages.error(request, "User Name Must Be 10 Characters.")
            return redirect("signup")
        if not user_name.isalnum():
            messages.error(
                request, "Username Should Only Contain Letters And Numbers.")
            return redirect("signup")
        if password != c_password:
            messages.error(
                request, "Password do Not Match Please Confirm The password.")
            return redirect("signup")

        myuser = TechUser.objects.create_user(user_name, e_mail, password)
        myuser.save()
        new_user = authenticate(username=user_name, password=password)
        login(request, new_user)
        messages.success(request, "sign up successfully.now you log in....")
        # subject = 'estore'
        # message = f'1successful sigup'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [e_mail]
        # send_mail(subject, message, email_from, recipient_list)
        return redirect("home")
    return render(request, 'user/register.html')


class ContactTemplateView(TemplateView):
    template_name = 'user/contact-us.html'
