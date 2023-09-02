from django.urls import path
from . import views


urlpatterns = [
    path('Racks/', views.index, name='index'),
    path('Racks/rack1/', views.rack1, name='rack1'),
    path('Racks/rack2/', views.rack2, name='rack2'),
    path('Racks/rack3/', views.rack3, name='rack3'),
    path('Racks/rack4/', views.rack4, name='rack4'),
    path('Racks/rack5/', views.rack5, name='rack5'),
    path('link/', views.link, name='link'),
    path('', views.home, name='home'),
    path('add_item/', views.add_item, name='add_item'),
    # path('boxitems/', views.boxitems, name='boxitems'),
    path('box_click/<int:feature_id>/', views.box_click, name='box_click'),
    path('add_box/', views.add_box, name='add_box'),
    path('Racks/rack1/scanner',views.scanner,name='scanner'),
    path('Racks/rack2/scanner',views.scanner,name='scanner'),
    path('Racks/rack3/scanner',views.scanner,name='scanner'),
    path('Racks/rack4/scanner',views.scanner,name='scanner'),
    path('Racks/rack5/scanner',views.scanner,name='scanner'),
    path('Racks/home', views.home, name='home'),
    
    
]
