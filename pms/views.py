from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

def index(request):
    context = { 'title' : "This is test" }
    return render(request, 'index.html', context)

def test(request):
    context = { 'blog_entries' : [ { 'title': 'Test man', 'body': 'This is a simple test' }, { 'title': 'Okay bro', 'body': 'I got it' } ] }
    return render(request, 'tests/sub.html', context)