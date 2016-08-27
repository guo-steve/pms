from django.shortcuts import render

from .models import Contact

def index(request):
    context = {
        'title': 'Customers',
        'page_header': 'Customers list',
        'page_description': 'List all customers you can see',
    }
    return render(request, 'customers/index.html', context)

def ajax(request):
    data = {"data": []}
    for c in Contact.objects.select_related():
        data['data'].append({
            'id': c.pk,
            'name': c.name,
            'order_number': c.order_number,
            'quantity': o.quantity,
            'customer': o.customer.name,
            'country': o.customer.country.name,
            'date': str(o.creation_date),
        })
    return HttpResponse(json.dumps(data), content_type='application/json')
