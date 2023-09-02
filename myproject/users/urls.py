from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login1/', views.login1, name='login1'),

    # Add more URL patterns for other views if needed
]
