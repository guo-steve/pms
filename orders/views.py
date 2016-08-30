from django.shortcuts import render
from django.template import Template, RequestContext
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.core.urlresolvers import reverse
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

def orders(request):
    if request.method == 'POST' and request.META['CONTENT_TYPE'] == 'application/json':
        pass
    else:
        context = {
            'title' : 'Orders',
            'page_header' : 'Orders list',
            'page_description': 'The list of all orders',
            'breadcrumb' : [
                { 'label': 'Orders', 'url': reverse('orders:index') },
            ],
            'box_header': 'Orders',
        }
        return render(request, 'orders/index.html', context)

def orders_ajax(request):
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
            'uri': reverse('orders:detail', args=[o.pk]),
        })
    return HttpResponse(json.dumps(data), content_type='application/json')

def orders_detail(request, order_id):
    try:
        o = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        raise Http404("Order does not exist")

    context = {
        'title': 'Order Detail',
        'page_header' : 'Order detail',
        'breadcrumb': [
            { 'label': 'Detail', 'url': reverse('orders:detail', args=[order_id]) },
            { 'label': 'Orders', 'url': reverse('orders:index') },
        ],
        'order': o,
    }
    return render(request, 'orders/order_detail.html', context)

def data_batches(request):
    if request.method == 'POST' and request.META['CONTENT_TYPE'] == 'application/json':
        pass
    else:
        context = {
            'title' : 'Data Batches',
            'page_header' : 'Data batches list'
        }
        return render(request, 'orders/data_batches.html', context)

def data_batches_ajax(request, order_id=None):
    data = {"data": []}
    for d in DataBatch.objects.select_related():
        data['data'].append({
            'id': d.pk,
            'country': d.country(),
            'batch_number': d.batch_number,
            'quantity': d.quantity,
            'order': d.order.name,
            'publish_date': str(d.publish_date),
        })
    return HttpResponse(json.dumps(data), content_type='application/json')

def data_batches_detail(request):
    context = {
        'title': 'Order Detail',
        'page_header' : 'Order detail',
        'breadcrumb': [
            { 'label': 'Orders', 'url': '' },
        ]
    }
    return render(request, 'orders/order_detail.html', context)


