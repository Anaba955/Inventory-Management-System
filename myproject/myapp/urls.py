from django.urls import include, path
from . import views



urlpatterns = [
    
    path('Racks/', views.index, name='index'),
    # path('AdminRack/', views.adminInd, name='adminInd'),
    path('rack1', views.rack1, name='rack1'),
    path('rack2', views.rack2, name='rack2'),
    path('rack3', views.rack3, name='rack3'),
    path('rack4', views.rack4, name='rack4'),
    path('rack5', views.rack5, name='rack5'),
    path('link/', views.link, name='link'),
    path('', views.home, name='home'),
    path('add_item', views.add_item, name='add_item'),
    path('box_click/<int:feature_id>/', views.box_click, name='box_click'),
    path('add_box', views.add_box, name='add_box'),
    path('scanner/<int:feature_id>', views.scanner, name='scanner'),
    path('ruq/', views.ruq, name='ruq'),
    path('simple',views.simple,name='simple'),
    path('quantity/<int:product_id>', views.quantity, name='quantity'),
    path('sub/<int:product_id>', views.sub, name = 'sub'),
    path('Racks/home', views.home, name='home'),  
    path('search/', views.search_item, name='search_item'),
    # path('allQR', views.allQR, name = 'allQR'),
    path('anchor/', views.anchor, name='anchor'),
    path('allQR/', views.allQR, name='allQR'),
    path('del_box/<int:feature_id>', views.del_box, name='del_box'),    
]
