from django.http.response import HttpResponse
from django.shortcuts import render

def tdash(request):
    return render(request, 'tdash.html')



def index(request):
    return render(request, 'tdash.html')

def exam1 (request):
      return render(request, 'exam1.html')

def exam2 (request):
      return render(request, 'exam2.html')

def endterm (request):
      return render(request, 'endterm.html')

def finalreport (request):
      return render(request, 'finalreport.html')


