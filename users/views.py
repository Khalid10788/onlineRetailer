from django.http import HttpResponseRedirect
from django.shortcuts import render
from allauth.account.views import SignupView, LoginView, PasswordResetView, PasswordResetDoneView
from users.forms import CustomSignupForm, CustomLoginForm


# Create your views here.


class loginView(LoginView):
    template_name = ''
    form_class = CustomLoginForm


class signupView(SignupView):
    template_name = 'online_retailer/account/register.html'
    form_class = CustomSignupForm


def index(request):
    return render(request, 'home/index.html', {"": ""})