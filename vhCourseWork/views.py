from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader

from vhCourseWork.models import *


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def client(request, client_id):
    client_data = get_object_or_404(Client, pk=client_id)
    template = loader.get_template('organisation/organisation_details.html')
    context = {
        'client': client_data,
    }
    return HttpResponse(template.render(context, request))


def clients(request):
    clients_data = Client.objects.all()
    template = loader.get_template('organisation/organisations_list.html')
    context = {
        'org_type': "client",
        'clients': clients_data,
    }
    return HttpResponse(template.render(context, request))


def client_edit(request, client_id):
    client_data = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        client_data.name = request.POST.get('name')
        client_data.director = request.POST.get('director')
        client_data.address = request.POST.get('address')
        client_data.phone = request.POST.get('phone')
        client_data.tin = request.POST.get('tin')
        client_data.bank_details = request.POST.get('bank_details')
        client_data.notes = request.POST.get('notes')
        client_data.save()
        return HttpResponseRedirect('/clients')
    else:
        template = loader.get_template('organisation/organisation_data_manipulation.html')
        context = {
            'org_type': "client",
            'org_data': client_data,
        }
        return HttpResponse(template.render(context, request))


def client_remove(request, client_id):
    client_data = get_object_or_404(Client, pk=client_id).delete()
    return HttpResponseRedirect('/clients')


def client_add(request):
    if request.method == 'POST':
        client_data = Client()
        client_data.name = request.POST.get('name')
        client_data.director = request.POST.get('director')
        client_data.address = request.POST.get('address')
        client_data.phone = request.POST.get('phone')
        client_data.bank_details = request.POST.get('bank_details')
        client_data.tin = request.POST.get('tin')
        client_data.notes = request.POST.get('notes')
        client_data.save()
        return HttpResponseRedirect('/clients')
    else:
        template = loader.get_template('organisation/organisation_data_manipulation.html')
        context = {
            'org_type': "client",
        }
        return HttpResponse(template.render(context, request))


def manufacturers(request):
    manufacturers_data = Manufacturer.objects.all()
    template = loader.get_template('organisation/organisations_list.html')
    context = {
        'org_type': "manufacturer",
        'manufacturers': manufacturers_data,
    }
    return HttpResponse(template.render(context, request))


def manufacturer(request, manufacturer_id):
    manufacturer_data = get_object_or_404(Manufacturer, pk=manufacturer_id)
    template = loader.get_template('organisation/organisation_details.html')
    context = {
        'manufacturer': manufacturer_data,
    }
    return HttpResponse(template.render(context, request))


def manufacturer_add(request):
    if request.method == 'POST':
        manufacturer_data = Manufacturer()
        manufacturer_data.name = request.POST.get('name')
        manufacturer_data.director = request.POST.get('director')
        manufacturer_data.accountant = request.POST.get('accountant')
        manufacturer_data.address = request.POST.get('address')
        manufacturer_data.phone = request.POST.get('phone')
        manufacturer_data.fax = request.POST.get('fax')
        manufacturer_data.bank_details = request.POST.get('bank_details')
        manufacturer_data.tin = request.POST.get('tin')
        manufacturer_data.notes = request.POST.get('notes')
        manufacturer_data.save()
        return HttpResponseRedirect('/manufacturers')
    else:
        template = loader.get_template('organisation/organisation_data_manipulation.html')
        context = {
            'org_type': "manufacturer",
        }
        return HttpResponse(template.render(context, request))


def manufacturer_edit(request, manufacturer_id):
    manufacturer_data = get_object_or_404(Manufacturer, pk=manufacturer_id)
    if request.method == 'POST':
        manufacturer_data.name = request.POST.get('name')
        manufacturer_data.director = request.POST.get('director')
        manufacturer_data.accountant = request.POST.get('accountant')
        manufacturer_data.address = request.POST.get('address')
        manufacturer_data.phone = request.POST.get('phone')
        manufacturer_data.fax = request.POST.get('fax')
        manufacturer_data.bank_details = request.POST.get('bank_details')
        manufacturer_data.tin = request.POST.get('tin')
        manufacturer_data.notes = request.POST.get('notes')
        manufacturer_data.save()
        return HttpResponseRedirect('/manufacturers')
    else:
        template = loader.get_template('organisation/organisation_data_manipulation.html')
        context = {
            'org_type': "manufacturer",
            'org_data': manufacturer_data,
        }
        return HttpResponse(template.render(context, request))


def manufacturer_remove(request, manufacturer_id):
    manufacturer_data = get_object_or_404(Manufacturer, pk=manufacturer_id).delete()
    return HttpResponseRedirect('/manufacturers')


def suppliers(request):
    suppliers_data = Supplier.objects.all()
    template = loader.get_template('organisation/organisations_list.html')
    context = {
        'org_type': "supplier",
        'suppliers': suppliers_data,
    }
    return HttpResponse(template.render(context, request))


def supplier_add(request):
    if request.method == 'POST':
        supplier_data = Supplier()
        supplier_data.name = request.POST.get('name')
        supplier_data.director = request.POST.get('director')
        supplier_data.accountant = request.POST.get('accountant')
        supplier_data.address = request.POST.get('address')
        supplier_data.phone = request.POST.get('phone')
        supplier_data.fax = request.POST.get('fax')
        supplier_data.bank_details = request.POST.get('bank_details')
        supplier_data.tin = request.POST.get('tin')
        supplier_data.notes = request.POST.get('notes')
        supplier_data.save()
        return HttpResponseRedirect('/suppliers')
    else:
        template = loader.get_template('organisation/organisation_data_manipulation.html')
        context = {
            'org_type': "supplier",
        }
        return HttpResponse(template.render(context, request))


def supplier_edit(request, supplier_id):
    supplier_data = get_object_or_404(Supplier, pk=supplier_id)
    if request.method == 'POST':
        supplier_data.name = request.POST.get('name')
        supplier_data.director = request.POST.get('director')
        supplier_data.accountant = request.POST.get('accountant')
        supplier_data.address = request.POST.get('address')
        supplier_data.phone = request.POST.get('phone')
        supplier_data.fax = request.POST.get('fax')
        supplier_data.bank_details = request.POST.get('bank_details')
        supplier_data.tin = request.POST.get('tin')
        supplier_data.notes = request.POST.get('notes')
        supplier_data.save()
        return HttpResponseRedirect('/suppliers')
    else:
        template = loader.get_template('organisation/organisation_data_manipulation.html')
        context = {
            'org_type': "supplier",
            'org_data': supplier_data,
        }
        return HttpResponse(template.render(context, request))


def supplier_remove(request, supplier_id):
    supplier_data = get_object_or_404(Supplier, pk=supplier_id).delete()
    return HttpResponseRedirect('/suppliers')


def supplier(request, supplier_id):
    supplier_data = get_object_or_404(Supplier, pk=supplier_id)
    template = loader.get_template('organisation/organisation_details.html')
    context = {
        'supplier': supplier_data,
    }
    return HttpResponse(template.render(context, request))
