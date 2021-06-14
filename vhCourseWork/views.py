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
    template = loader.get_template('client/client.html')
    context = {
        'client': client_data,
    }
    return HttpResponse(template.render(context, request))


def clients(request):
    clients_data = Client.objects.all()
    template = loader.get_template('client/clients.html')
    context = {
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
        client_data.TIN = request.POST.get('TIN')
        client_data.notes = request.POST.get('notes')
        client_data.save()
        return HttpResponseRedirect('/clients')
    else:
        template = loader.get_template('client/client_edit.html')
        context = {
            'client': client_data,
        }
        return HttpResponse(template.render(context, request))




def client_remove(request, client_id):
    client_data = get_object_or_404(Client, pk=client_id)
    template = loader.get_template('client/client_remove.html')
    context = {
        'client': client_data,
    }
    return HttpResponse(template.render(context, request))
