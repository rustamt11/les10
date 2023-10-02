from django.shortcuts import render

from dating.models import User


def first_page(request):
    if request.method == 'POST':
        name = request.POST.get("user")
        surname = request.POST.get("surname")
        age = request.POST.get("age")
        User.objects.create(name=name,
                            surname=surname,
                            age=age)

    return render(request, 'addrest.html')


def last_page(requset,id_user):
    context = {'users':User.objects.get(pk = id_user)}
    return render(requset,'index.html',context = context)


def chec_profil(request):
    context={'users':User.objects.all()}
    return render(request,'profil.html',context=context)