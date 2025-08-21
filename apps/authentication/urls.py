from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='default'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin')
]