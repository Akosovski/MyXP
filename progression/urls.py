from . import views
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="progression"),
    path('authentication/', include('authentication.urls')),
    path('add-activity', views.add_activity, name="add-activity"),
    path('activity-list', views.activity_list, name="activity-list"),
    path('close-modal', views.close_modal, name="close-modal"),
]