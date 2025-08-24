from django.urls import path, include
from . import views



urlpatterns = [
    path('daily/', views.daily, name='daily'),
    path('daily/add_task/', views.add_task, name='add_task'),
    path('daily/get_task/', views.get_task, name="get_task"),
    path('daily/delete_task/', views.delete_task, name='delete_task'),
    path('daily/edit_task/', views.edit_task, name="edit_task"),
    path('daily/edit_submission/', views.save_edit_task, name='save_edit_task'),
    path('all/', views.all, name="all"),
    path('important/', views.important, name="important"),
    path('completed/', views.completed, name="completed"),
]