from django.urls import path, include

urlpatterns = [
    path('product/', include('goods.back-office.product.urls')),
    path('category/', include('goods.back-office.category.urls')),
    path('enter/', include('goods.back-office.enter.urls')),
    path('banner/', include('goods.back-office.banner.urls')),
    path('info/', include('goods.back-office.info.urls')),
]