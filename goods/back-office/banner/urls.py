from django.urls import path
from . import views

urlpatterns = [
    path('banners/', views.listBanner, name='listBanner'),
    path('banners/<int:id>/', views.detailBanner, name='detailBanner'),
    path('banners/create/', views.createBanner, name='createBanner'),
    path('banners/<int:id>/delete/', views.deleteBanner, name='deleteBanner'),
    path('banners/<int:id>/update/', views.updateBanner, name='updateBanner'),
]