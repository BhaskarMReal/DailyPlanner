from django.urls import path, include
from . import views



urlpatterns = [
    path('daily/', views.daily, name='daily'),
    path('daily/add_task/', views.add_task, name='add_task'),
    path('daily/get_task/', views.get_task, name="get_task")
]