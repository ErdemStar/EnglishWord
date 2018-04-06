# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import *
from django.shortcuts import render
from models import Words

# Create your views here.


def Yonlendir(request):
    return HttpResponseRedirect("Index")

def Index(request):
    return render(request,"Index.html", {})

def KelimeEkle(request):
    if request.method == "GET":
        return render(request,"KelimeEkle.html", {})
    elif request.method == "POST":
        eword = request.POST.get("eword")
        tword = request.POST.get("tword")
        tur   = request.POST.get("tur")
        cumle = request.POST.get("cumle")

        if Words.objects.filter(englishWord=eword,turkishWord=tword,type=tur) == "QuerySet[]":
            return render(request, "KelimeEkle.html", {"Err":"alert('Boyle bir kayıt vardır')"})
        else:
            New = Words(englishWord=eword, turkishWord=tword,type=tur,sentence= cumle)
            New.save()
            return render(request, "KelimeEkle.html", {})


def KelimeListele(request):
    if request.method == "GET":
        Arr = Words.objects.order_by("englishWord")
        return render(request,"KelimeListele.html", {"Arr":Arr})