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

        if eword and tword and tur and cumle != "":
            query = "select * from Manage_Words"

            var = Words.objects.raw(query)

            if eword and tword and tur in var:
                return render(request, "KelimeEkle.html", {"Er":"alert('Böyle bir kayıt vardır.')"})
            else:
                New = Words(englishWord=eword, turkishWord=tword,type=tur,sentence= cumle)
                New.save()
                return render(request, "KelimeEkle.html", {})


def KelimeListele(request):
    if request.method == "GET":
        query = "select * from Manage_Words"
        Arr = Words.objects.raw(query)
        return render(request,"KelimeListele.html", {"Arr":Arr})