from django.shortcuts import render

def index(request):
    context = {
        'title': 'Documents',
        'page_header': 'Documents list',
    }
    return render(request, 'documents/index.html', context)