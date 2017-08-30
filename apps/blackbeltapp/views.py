from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages





def index(request):
    return render(request , 'blackbeltapp/index.html')

def register(request):
    User.objects.validate(request, request.POST)
    return redirect('/')

def logmein(request, id):
    # print id, 'yah'
    users = User.objects.all()

    context = {
     'all_users': users,
     'current_user': User.objects.get(id = id)
    }
    if not User.objects.filter(email=request.POST['loginemail']):
        return HttpResponse('Sorry Wrong Email Address or password')
    else:
        return render(request, 'blackbeltapp/friends.html', context)

def show_user(request, id):
    print id, 'show user route'
    if request.method == 'POST':
     user = User.objects.get(id=id)
    return render(request, '/friends/'+id, {'user':user})

def login(request):
    print 'login route'
    result = User.objects.validate_login(request.POST)
    print result
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, 'You got it')
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'blackbeltapp/friends.html', context)
