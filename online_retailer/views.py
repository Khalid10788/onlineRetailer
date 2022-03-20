from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def chome(request):
    return HttpResponse("<h1>this is custome home page</h1>")