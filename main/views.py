from django.http import HttpResponse
from django.core import serializers
from main.models import Inventory
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.shortcuts import render

def show_main(request):
    inventories = Inventory.objects.all()
    context = {
        'name': 'Sekar Gandes Dianti',
        'class': 'PBP D',
        'products': inventories
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "create_product.html", context)


def show_xml(request):
    data = Inventory.objects.all()
    return HttpResponse(serializers.serialize('xml', data), 
                        content_type= 'application/xml')

def show_json(request):
    data = Inventory.objects.all()
    return HttpResponse(serializers.serialize('json', data),
                        content_type='application/json')

def show_xml_by_id(request, id):
    data = Inventory.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), 
                        content_type= 'application/xml')

def show_json_by_id(request, id):
    data = Inventory.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data),
                        content_type='application/json')