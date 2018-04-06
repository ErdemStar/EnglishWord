# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import *
from django.shortcuts import render

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
        cumle = request.POST.get("umle")

        if eword and tword and tur and cumle != "":
            query = "select * from Manage_Words"

            var = Words.objects.raw(query)

            if eword and tword and tur in var:
                return render(request, "KelimeEkle.html", {"error":"Eklediğin fiilin aynı anlamadında aynı "
                                                                   "türünde bir kayıt mevcut"})
            else:
                New = Words(Eword="eee", TMeaning="Ahmet",Type="Veli",Sentence= "Cemal")

def KelimeListele(request):
    if request.method == "GET":
        query = "select * from Manage_Words"
        Arr = Words.objects.raw(query)
        return render(request,"KelimeListele.html", {"Arr":Arr})