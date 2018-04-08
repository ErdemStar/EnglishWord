# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import *
from django.shortcuts import render
from models import Words
import random

#-------------------
allWord   = []


def GetLast5Word():
    Last5 = Words.objects.all()
    Last5Word=[]
    for i in Last5[len(Last5)-5:]:
        Last5Word.append(i)
    return Last5Word
#-------------------


def Yonlendir(request):
    return HttpResponseRedirect("Index")

def Index(request):
    return render(request,"Index.html", {})

def KelimeEkle(request):
    if request.method == "GET":
        return render(request,"KelimeEkle.html", {"Last5Word":GetLast5Word()})
    elif request.method == "POST":
        eword = request.POST.get("eword")
        tword = request.POST.get("tword")
        tur   = request.POST.get("tur")
        cumle = request.POST.get("cumle")
        state=True

        #if Words.objects.filter(englishWord=eword,turkishWord=tword,type=tur) == "QuerySet[]":
        #    return render(request, "KelimeEkle.html", {"Err":"alert('Boyle bir kayıt vardır')"})
        if True:
            getir = Words.objects.all()
            for i in getir:
                if i.englishWord == eword and i.turkishWord == tword and i.type==tur:
                    state=False
                    alert= "alert('Boyle bir kayıt vardır')"
            if state:
                New = Words(englishWord=eword, turkishWord=tword,type=tur,sentence= cumle)
                New.save()
                alert ="alert('Kayıt Eklendi')"
        return render(request, "KelimeEkle.html",{"Err":alert , "Last5Word":GetLast5Word()})


def KelimeListele(request):
    if request.method == "GET":
        Arr = Words.objects.order_by("englishWord")
        return render(request,"KelimeListele.html", {"Arr":Arr})


def KelimeSorma(request):
    if request.method == "GET":
        global allWord
        getir = Words.objects.all()
        for i in getir:
            allWord.append(i)
        random.shuffle(allWord)
        return render(request,"KelimeSorma.html",{"arr":allWord[:5]})
    elif request.method == "POST":
        global allWord
        score = 0
        t1 = request.POST["t1"].encode('utf-8')
        t2 = request.POST["t2"].encode("utf-8")
        t3 = request.POST["t3"].encode("utf-8")
        t4 = request.POST["t4"].encode("utf-8")
        t5 = request.POST["t5"].encode("utf-8")
        for i in allWord[:5]:
            if t1 in i.turkishWord.encode('utf-8'):
                score+=20
            elif t2 in i.turkishWord.encode('utf-8'):
                score+=20
            elif t3 in i.turkishWord.encode('utf-8'):
                score += 20
            elif t4 in i.turkishWord.encode('utf-8'):
                score += 20
            elif t5 in i.turkishWord.encode('utf-8'):
                score += 20

        return render(request, "KelimeSorma.html", {"score": score,"arr":allWord[:5]})
