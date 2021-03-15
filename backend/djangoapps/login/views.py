import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections


def login(request):
    print('login')
    return render(request, 'login/login.html')

def api_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print('dasdasdsadsadasd')
    print("user =>>",username,password)
    return JsonResponse({'result':'success'})