from django.http.response import HttpResponse
from django.shortcuts import render

def tdash(request):
    return render(request, 'tdash.html')



def index(request):
    return render(request, 'tdash.html')

