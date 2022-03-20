from django.urls import path, include
from allauth.account.views import LogoutView,password_reset
from .views import signupView, loginView, index

urlpatterns = [
    # path('', index, name=''),
    path('home' , index, name='home'),
    path('signup' ,signupView.as_view(), name='account_signup'),
    path('login' , loginView.as_view(template_name = 'account/login.html'), name='login'),
    path('logout' , LogoutView.as_view(),name='logout'),
]