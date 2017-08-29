from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import auth




def index(request):
    return render(request , 'blackbeltapp/index.html')

def register(request):
    User.objects.validate(request, request.POST)
    return redirect('/')

def logmein(request, id):
    print id , '-------------------'
    user = User.objects.get(id=id)
    # users.full_name = request.POST['loginemail']
    # context = {
    #  'listallusers': User.objects.all(),
    # #  'user' : User.objects.get(id=request.POST['loginemail'])
    # # 'users.full_name' : request.POST['loginemail']
    # }
    if not User.objects.filter(email=request.POST['loginemail']):
        return HttpResponse('Sorry Wrong Email Address or password')
    else:
        user = User.objects.get(id=id)

        return redirect('friends/'+id)
