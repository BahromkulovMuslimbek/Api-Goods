from goods import models
from django.shortcuts import render, redirect


def listBanner(request):
    queryset = models.Banner.objects.all()
    context = {'queryset': queryset}
    return render(request, 'back-office/banner/list.html', context)


def detailBanner(request, id):
    banner, created = models.Banner.objects.get_or_create(id=id)
    context = {'banner': banner}
    return render(request, 'back-office/banner/detail.html', context)


def createBanner(request):
    if request.method == 'POST':
        title = request.POST['title']
        sub_title = request.POST.get('sub_title', '')
        img = request.FILES['img']
        is_active = request.POST.get('is_active', False) == 'on'

        banner, created = models.Banner.objects.get_or_create(
            title=title,
            defaults={
                'sub_title': sub_title,
                'img': img,
                'is_active': is_active,
            }
        )

        if not created:
            banner.sub_title = sub_title
            banner.img = img
            banner.is_active = is_active
            banner.save()

        return redirect('listBanner')
    
    return render(request, 'back-office/banner/create.html')


def deleteBanner(request, id):
    banner, created = models.Banner.objects.get_or_create(id=id)
    if not created:
        banner.delete()
    return redirect('listBanner')


def updateBanner(request, id):
    banner, created = models.Banner.objects.get_or_create(id=id)

    if request.method == 'POST':
        title = request.POST['title']
        sub_title = request.POST.get('sub_title', '')
        is_active = request.POST.get('is_active', False) == 'on'

        if 'img' in request.FILES:
            banner.img = request.FILES['img']

        banner.title = title
        banner.sub_title = sub_title
        banner.is_active = is_active
        banner.save()

        return redirect('listBanner')

    context = {'banner': banner}
    return render(request, 'back-office/banner/update.html', context)