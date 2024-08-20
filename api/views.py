from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from goods.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, UserSerializer



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
        return Response({'user': UserSerializer(user).data, 'message': "Royxatdan otish muvaffaqiyatli "}, status=status.HTTP_201_CREATED) 
    return Response({'errors': serializer.errors, 'message': "Royxatdan otishda xatolik"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({'token': token.key, 'message': "Siz tizimga muvaffaqiyatli kirdingiz"}, status=status.HTTP_200_OK)
    return Response({'error': "Kirish xatoligi", 'message': "Foydalanuvchi nomi yoki parol noto'g'ri"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request):
    request.auth.delete()
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)