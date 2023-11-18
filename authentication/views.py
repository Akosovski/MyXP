import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib import auth
from django.contrib.auth.models import Permission

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username=request.POST['username']
        password=request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, str(user) + ' successfully logged in!')
                    return redirect('progression')
            messages.error(request, 'No matching credentials!')
            return render(request, 'authentication/login.html')
        messages.error(request, 'No matching credentials!')
        return render(request, 'authentication/login.html')

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        return redirect('login')