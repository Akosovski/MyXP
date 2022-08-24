
from dataclasses import field
from django.contrib.auth.decorators import login_required
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse, HttpResponse
import datetime
import tempfile
from django.template.loader import render_to_string

@login_required(login_url = '/authentication/login')
def index(request):
    return render(request, 'progression/index.html')