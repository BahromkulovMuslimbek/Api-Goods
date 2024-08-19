from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required


@login_required
def myCart(request):
    cart, created = models.Cart.objects.get_or_create(author=request.user, is_active=True)


def paginator_page(data, num, request):
    paginator = Paginator(data.order_by('-id'), num)
    pages = request.GET.get('page')
    try:
        paginated_list = paginator.page(pages)
    except PageNotAnInteger:
        paginated_list = paginator.page(1)
    except EmptyPage:
        paginated_list = paginator.page(paginator.num_pages)
    return paginated_list

def main(request):
    banners = models.Banner.objects.all()
    category = models.Category.objects.all()
    last_img = models.ProductImg.objects.all()
    wishlist = models.WishList.objects.all()
    
    context = {}
    context['banners'] = banners
    context['categories'] = category
    context['products'] = paginator_page(last_img, 8 , request)
    context['wishlist'] = wishlist

    return render(request, 'index.html', context)


def user(request):
    return render(request, 'user/detail.html')
