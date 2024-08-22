from django.urls import path
from .views import ( CategoryListAPIView, CategoryDetailAPIView, CategoryDeleteAPIView, CategoryCreateAPIView, 
ProductListAPIView, ProductDetailAPIView, ProductCreateAPIView, ProductDeleteAPIView,  
MyCartAPIView, MainAPIView, UserDetailAPIView, 
BannerCreateView, BannerDeleteView, BannerListCreateView, BannerDetailView,
InfoCreateView, InfoDeleteView, InfoListCreateView, InfoDetailView,
OrderCreateView, OrderDeleteView, OrderListCreateView, OrderDetailView,
CartProductCreateView, CartProductDeleteView, CartProductListCreateView, CartProductDetailView, 
ProductEnterCreateView, ProductEnterDeleteView, ProductEnterListCreateView, ProductEnterDetailView, 
WishListCreateView, WishListDeleteView, WishListListCreateView, WishListDetailView,
login_view, register, logout_view )


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name='category-delete'),

    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete'),

    path('banners/', BannerListCreateView.as_view(), name='banner-list-create'),
    path('banners/<int:pk>/', BannerDetailView.as_view(), name='banner-detail'),
    path('banners/create/', BannerCreateView.as_view(), name='banner-create'),
    path('banners/delete/<int:pk>/', BannerDeleteView.as_view(), name='banner-delete'),

    path('info/', InfoListCreateView.as_view(), name='info-list-create'),
    path('info/<int:pk>/', InfoDetailView.as_view(), name='info-detail'),
    path('info/create/', InfoCreateView.as_view(), name='info-create'),
    path('info/delete/<int:pk>/', InfoDeleteView.as_view(), name='info-delete'),

    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),

    path('cartproducts/', CartProductListCreateView.as_view(), name='cartproduct-list-create'),
    path('cartproducts/<int:pk>/', CartProductDetailView.as_view(), name='cartproduct-detail'),
    path('cartproducts/create/', CartProductCreateView.as_view(), name='cartproduct-create'),
    path('cartproducts/delete/<int:pk>/', CartProductDeleteView.as_view(), name='cartproduct-delete'),

    path('productentries/', ProductEnterListCreateView.as_view(), name='productenter-list-create'),
    path('productentries/<int:pk>/', ProductEnterDetailView.as_view(), name='productenter-detail'),
    path('productentries/create/', ProductEnterCreateView.as_view(), name='productenter-create'),
    path('productentries/delete/<int:pk>/', ProductEnterDeleteView.as_view(), name='productenter-delete'),

    path('wishlist/', WishListListCreateView.as_view(), name='wishlist-list-create'),
    path('wishlist/<int:pk>/', WishListDetailView.as_view(), name='wishlist-detail'),
    path('wishlist/create/', WishListCreateView.as_view(), name='wishlist-create'),
    path('wishlist/delete/<int:pk>/', WishListDeleteView.as_view(), name='wishlist-delete'),

    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('api/logout/', logout_view, name='logout'),

    path('cart/', MyCartAPIView.as_view(), name='api_my_cart'),
    path('main/', MainAPIView.as_view(), name='api_main'),
    path('user/', UserDetailAPIView.as_view(), name='api_user'),

]