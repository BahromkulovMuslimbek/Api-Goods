from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.listInfo, name='listInfo'),
    path('info/<int:id>/', views.detailInfo, name='detailInfo'),
    path('info/create/', views.createInfo, name='createInfo'),
    path('info/update/<int:id>/', views.updateInfo, name='updateInfo'),
    path('info/delete/<int:id>/', views.deleteInfo, name='deleteInfo'),
]
