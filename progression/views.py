from dataclasses import field
from django.contrib.auth.decorators import login_required
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.admin import User
from .models import Activity
from django.contrib import messages
from django.core.paginator import Paginator
from django.template.loader import render_to_string

@login_required(login_url = '/authentication/login')
def index(request):
    activities = Activity.objects.all()
    recents = Activity.objects.order_by('-updated_at')[:3]

    total_xp = 0
    for activity in activities:
        total_xp += activity.activity_xp
    
    if total_xp < 1000:
        shown_xp = total_xp
    else:
        shown_xp = total_xp % 1000

    xp_level = total_xp / 1000
    bar_width = shown_xp / 10

    int_level = int(xp_level)

    context = {
        'activities': activities,
        'shown_xp': shown_xp,
        'int_level': int_level,
        'bar_width': bar_width,
        'recents': recents,
    }
    return render(request, 'progression/index.html', context)

@login_required(login_url = '/authentication/login')
def add_activity(request):
    if request.method == 'POST':
        activity_name = request.POST.get('name')
        activity_xp = request.POST.get('xp')
        activity_summary = request.POST.get('summary')

        if not activity_name:
            messages.error(request, 'Incorrect name!')
            return render(request, 'progression/index.html')
        
        if not activity_xp:
            messages.error(request, 'Incorrect points!')
            return render(request, 'progression/index.html')
        
        if not activity_summary:
            messages.error(request, 'Incorrect summary!')
            return render(request, 'progression/index.html')
        
        Activity.objects.create(owner=request.user, activity_name=activity_name, activity_xp=activity_xp, activity_summary=activity_summary)
        messages.success(request, 'Successfully added activity!')
        
        return redirect('progression')

def close_modal(request):
    return redirect('progression')

@login_required(login_url = '/authentication/login')
def activity_list(request):
    activities = Activity.objects.order_by('-updated_at')
    paginator = Paginator(activities, 15)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)

    context = {
        'activities': activities,
        'page_obj': page_obj,
    }
    return render(request, 'progression/activity_list.html', context)

@login_required(login_url = '/authentication/login')
def search_activity(request, id):
    activities = Activity.objects.all()
    context = {
        'activities': activities
    }
    return render(request, 'progression/search_activity.html', context)

@login_required(login_url = '/authentication/login')
def view_detail(request, id):
    activity = Activity.objects.get(pk=id)
    context = {
        'activity': activity
    }
    return render(request, 'progression/view_detail.html', context)

def delete_activity(request, id):
    activity = Activity.objects.get(pk=id)
    activity.delete()

    messages.success(request, 'Activity Deleted.')
    return redirect('activity-list')
