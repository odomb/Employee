from django.http import HttpResponse
from django.shortcuts import render


def room(request):
    print('hi')
    return HttpResponse ("<h1>Hello folks</h1>")
def home(request):
    return render(request,"about.html",{})

