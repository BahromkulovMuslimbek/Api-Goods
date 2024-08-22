from django.urls import path
from .views import CategoryListAPIView, CategoryDetailAPIView, CategoryDeleteAPIView, CategoryCreateAPIView, ProductListAPIView, ProductDetailAPIView, ProductCreateAPIView, ProductDeleteAPIView,  MyCartAPIView, MainAPIView, UserDetailAPIView, login_view, register, logout_view


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name='category-delete'),

    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete'),

    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('api/logout/', logout_view, name='logout'),

    path('cart/', MyCartAPIView.as_view(), name='api_my_cart'),
    path('main/', MainAPIView.as_view(), name='api_main'),
    path('user/', UserDetailAPIView.as_view(), name='api_user'),

]