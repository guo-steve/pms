from django.shortcuts import render
from django.template import Template, RequestContext
from django.http import HttpResponse
from django.utils import timezone
from .models import Order, DataBatch
import json

def hello(request):
    if request.method == 'POST' and request.META['CONTENT_TYPE'] == 'application/json':
        return HttpResponse(json.dumps({ "content": "Hello orders" }), content_type="application/json")
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
            'title' : 'Orders'
        }
        return render(request, 'orders/index.html', context)

def ajax(request):
    data = {"data": []}
    for o in Order.objects.select_related():
        data['data'].append({
            'id': o.pk,
            'name': o.name,
            'order_number': o.order_number,
            'quantity': o.quantity,
            'customer': o.customer.name,
            'country': o.customer.country.name,
            'date': str(o.creation_date),
        })
    return HttpResponse(json.dumps(data), content_type='application/json')
