from django.urls import path, include
from goods import views

urlpatterns = [
    path('', views.main, name='index'),
    path('authentication/', include('goods.authentication.urls')),
    path('back-office/', include('goods.back-office.urls')),
    path('user/', include('goods.user.urls')), 
]