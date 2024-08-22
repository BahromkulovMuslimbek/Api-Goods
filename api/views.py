from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from goods.models import Product, Category, Cart, Banner, ProductImg, WishList
from .serializers import ProductSerializer, CategorySerializer, UserSerializer, CartSerializer, BannerSerializer, ProductImgSerializer, WishListSerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'user': UserSerializer(user).data, 'message': "Регистрация успешна"}, status=status.HTTP_201_CREATED)
    return Response({'errors': serializer.errors, 'message': "Ошибка при регистрации"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({'token': token.key, 'message': "Успешный вход в систему"}, status=status.HTTP_200_OK)
    return Response({'error': "Ошибка входа", 'message': "Неверное имя пользователя или пароль"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_view(request):
    if request.auth:
        request.auth.delete()
        logout(request)
        return Response({'message': 'Вы успешно вышли из системы'}, status=status.HTTP_200_OK)
    return Response({'error': 'Вы не авторизованы'}, status=status.HTTP_400_BAD_REQUEST)


class MyCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = Cart.objects.get_or_create(author=request.user, is_active=True)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class MainAPIView(APIView):

    def get(self, request):
        banners = Banner.objects.all()
        categories = Category.objects.all()
        product_images = ProductImg.objects.all()
        wishlist = WishList.objects.all()
        
        banner_serializer = BannerSerializer(banners, many=True)
        category_serializer = CategorySerializer(categories, many=True)
        product_serializer = ProductImgSerializer(product_images, many=True)
        wishlist_serializer = WishListSerializer(wishlist, many=True)
        
        data = {
            'banners': banner_serializer.data,
            'categories': category_serializer.data,
            'products': product_serializer.data,
            'wishlist': wishlist_serializer.data,
        }
        
        return Response(data)


class UserDetailAPIView(APIView):

    def get(self, request):
        return Response({"message": "User detail endpoint"})
    