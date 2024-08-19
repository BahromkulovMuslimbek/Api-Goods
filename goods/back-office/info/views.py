from goods import models
from django.shortcuts import render, redirect


def listInfo(request):
    queryset = models.Info.objects.all()
    return render(request, 'back-office/info/list.html', {'queryset': queryset})


def detailInfo(request, id):
    info = models.Info.objects.get(id=id)
    return render(request, 'back-office/info/detail.html', {'info': info})


def createInfo(request):
    if request.method == 'POST':
        info = models.Info.objects.create(
            phone=request.POST['phone'],
            address=request.POST['address'],
            copyright=request.POST['copyright'],
            facebook_url=request.POST['facebook_url'],
            twitter_url=request.POST['twitter_url'],
            linkedin_url=request.POST['linkedin_url']
        )
        return redirect('listInfo')
    return render(request, 'back-office/info/create.html')


def deleteInfo(request, id):
    info = models.Info.objects.get(id=id)
    info.delete()
    return redirect('listInfo')


def updateInfo(request, id):
    info = models.Info.objects.get(id=id)
    if request.method == 'POST':
        info.phone = request.POST['phone']
        info.address = request.POST['address']
        info.copyright = request.POST['copyright']
        info.facebook_url = request.POST['facebook_url']
        info.twitter_url = request.POST['twitter_url']
        info.linkedin_url = request.POST['linkedin_url']
        info.save()
        return redirect('listInfo')
    return render(request, 'back-office/info/update.html', {'info': info})