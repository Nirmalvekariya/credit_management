from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Persons
from django.http import HttpResponseRedirect
from django import forms


def home(request):
    return render(request,"home.html",{})

def allusers(request):
    creditors = Persons.objects.all()
    return render(request, "allusers.html", {'persons_data': creditors})

def userdetails(request, user_id):
     userdata = Persons.objects.get(id=user_id)
     return render(request, "userdetails.html", {'users_data': userdata})

def transfer(request, user_id):
    name1 = request.POST.get('name1')
    if Persons.objects.filter(name=name1).exists():
        userdata1 = Persons.objects.get(id=user_id)
        userdata2 = Persons.objects.filter(name=name1)[0]
        credit1 = int(request.POST.get('credit1'))
        if (userdata1.name == userdata2.name):
            messages.error(request,"You can't Transfer to same Person")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if (userdata1.credites <= credit1):
            messages.error(request,"Credits must be Lesser then the remaining credits")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        userdata1.credites -= credit1
        userdata2.credites += credit1
        userdata1.transactions += 1
        userdata2.transactions += 1

        userdata2.save()
        userdata1.save()

        return HttpResponseRedirect('/allusers/')
    else:
        messages.error(request,"User Does not exists")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


