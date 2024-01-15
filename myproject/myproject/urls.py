"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from rack import views as rack_views
from rack2 import views as rack2_views
from rack3 import views as rack3_views
from rack4 import views as rack4_views
from rack5 import views as rack5_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    # path('Racks/', include('rack.urls')),
    # path('rack1/', rack_views.rack1, name='rack1'),
    # path('rack2/', rack2_views.rack2, name='rack2'),
    # path('rack3/', rack3_views.rack3, name='rack3'),
    # path('rack4/', rack4_views.rack4, name='rack4'),
    # path('rack5/', rack5_views.rack5, name='rack5'),
    # path('rack2/', include('rack2.urls')),
    # path('rack3/', include('rack3.urls')),
    # path('rack4/', include('rack4.urls')),
    # path('rack5/', include('rack5.urls')),
    # path('scanner', include('scanner.urls')),
    path('signup/', user_views.signup, name='signup'),
    path('login1/', user_views.login1, name='login1'),
    path('users/', include('users.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)