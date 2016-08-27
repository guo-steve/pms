from django.shortcuts import render
from django.template import Template, RequestContext
from django.http import HttpResponse

def hello(request):
    if request.method == 'POST' and request.META['CONTENT_TYPE'] == 'application/json':
        return HttpResponse(json.dumps({ "content": "Hello projects" }), content_type="application/json")
    else:
        ts = """<html><body>
        <h1>Hello orders!</h1>
        <pre>CSRF_Token: {{ csrf_token }}<br/>Current time: {{ now }}</pre> {% csrf_token %}
        </body></html>"""
        t = Template(ts)
        c = RequestContext(request, {"now": timezone.now()})
        return HttpResponse(t.render(c))

def index(request):
    if request.method == 'POST' and request.META['CONTENT_TYPE'] == 'application/json':
        pass
    else:
        context = {
            'title' : 'Orders',
            'page_header' : 'Orders list'
        }
        return render(request, 'orders/index.html', context)