from dataclasses import field
from django.contrib.auth.decorators import login_required
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.admin import User
from .models import Activity
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse, HttpResponse
import datetime
import tempfile
from django.template.loader import render_to_string

@login_required(login_url = '/authentication/login')
def index(request):
    activities = Activity.objects.all()
    paginator = Paginator(activities, 10)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'progression/index.html')

@login_required(login_url = '/authentication/login')
def add_activity(request):

    if request.method == 'POST':
        activity_name = request.POST.get('name')
        activity_xp = request.POST.get('xp')
        activity_summary = request.POST.get('summary')
        activity_date = request.POST.get('date')

        if not activity_name:
            messages.error(request, 'Incorrect name!')
            return render(request, 'progression/index.html')
        
        if not activity_xp:
            messages.error(request, 'Incorrect points!')
            return render(request, 'progression/index.html')
        
        if not activity_summary:
            messages.error(request, 'Incorrect summary!')
            return render(request, 'progression/index.html')
        
        if not activity_date:
            messages.error(request, 'Incorrect date!')
            return render(request, 'progression/index.html')
        
        Activity.objects.create(owner=request.user, activity_name=activity_name, activity_xp=activity_xp, activity_summary=activity_summary, activity_date=activity_date)
        messages.success(request, 'Successfully added activity!')
        return render(request, 'progression/index.html')