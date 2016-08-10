from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

def index(request):
    context = { 'title' : "This is test" }
    return render(request, 'index.html', context)