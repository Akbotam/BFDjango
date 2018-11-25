from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def login(request):
    #if request.method =='POST':
     #   if request.session.test_cookie_worked():
      #      request.session.delete_test_cookie()
       #     return HttpResponse("You're logged in")
        #else:
         #   return HttpResponse("Please enable cookies and try again")
        #request.session.set_test_cookie()
        #return render(request, 'auth_/login_form.html')
        u = User.objects.get(username = request.POST['username'])
        if u.password ==request.POST['password']:
            request.session['user_id'] = u.id
            return HttpResponse("You're logged in")
        else:
            return HttpResponse("Your username and password didn't match")

def register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
