from django.contrib.auth.decorators import login_required
from django.db.models import RestrictedError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from vhCourseWork.models import *


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


#
# detailed info related
#
@login_required
def client(request, client_id):
    client_data = get_object_or_404(Client, pk=client_id)
    template = loader.get_template('client/client.html')
    context = {
        'client': client_data,
    }
    return HttpResponse(template.render(context, request))


@login_required
def manufacturer(request, manufacturer_id):
    manufacturer_data = get_object_or_404(Manufacturer, pk=manufacturer_id)
    template = loader.get_template('manufacturer/manufacturer.html')
    context = {
        'manufacturer': manufacturer_data,
    }
    return HttpResponse(template.render(context, request))


@login_required
def supplier(request, supplier_id):
    supplier_data = get_object_or_404(Supplier, pk=supplier_id)
    template = loader.get_template('organisation/organisation_details.html')
    context = {
        'supplier': supplier_data,
    }
    return HttpResponse(template.render(context, request))


@login_required
def order(request, order_id):
    order_data = get_object_or_404(Order, pk=order_id)
    shipment_data = get_object_or_404(Shipment, pk=order_data)
    template = loader.get_template('order/order.html')
    context = {
        'order_data': order_data,
        'shipment_data': shipment_data,
    }
    return HttpResponse(template.render(context, request))


@login_required
def stock(request, stock_id):
    stock_data = get_object_or_404(Stock, pk=stock_id)
    template = loader.get_template('storage/stock.html')
    context = {
        'stock_data': stock_data,
    }
    return HttpResponse(template.render(context, request))


@login_required
def merchandise_info(request, merch_id):
    merch_data = get_object_or_404(Merchandise, pk=merch_id)
    template = loader.get_template('merchandise/merchandise_info.html')
    context = {
        'merch_data': merch_data,
    }
    return HttpResponse(template.render(context, request))


@login_required
def contract(request, contract_id):
    contract_data = get_object_or_404(Contract, pk=contract_id)
    template = loader.get_template('contract/contract.html')
    context = {
        'contract_data': contract_data,
    }
    return HttpResponse(template.render(context, request))


@login_required
def supply_order(request, order_id):
    order_data = get_object_or_404(SupplyOrder, pk=order_id)
    template = loader.get_template('supply_order/supply_order.html')
    context = {
        'order_data': order_data,
    }
    return HttpResponse(template.render(context, request))


#
# list view related
#
@login_required
def clients(request):
    clients_data = Client.objects.all()
    clients_data = clients_data.order_by('pk')
    template = loader.get_template('client/clients.html')
    context = {
        'clients': clients_data,
    }
    return HttpResponse(template.render(context, request))


@login_required
def manufacturers(request):
    manufacturers_data = Manufacturer.objects.all()

    template = loader.get_template('manufacturer/manufacturers.html')
    context = {
        'manufacturers': manufacturers_data,
    }
    return HttpResponse(template.render(context, request))


@login_required
def suppliers(request):
    suppliers_data = Supplier.objects.all()
    suppliers_data = suppliers_data.order_by('pk')
    template = loader.get_template('supplier/suppliers.html')
    context = {
        'org_type': "supplier",
        'suppliers': suppliers_data,
    }
    return HttpResponse(template.render(context, request))


@login_required
def orders(request):
    orders_data = Order.objects.all()
    orders_data = orders_data.order_by('pk')
    template = loader.get_template('order/orders.html')
    shipment_data = Shipment.objects.all()
    context = {
        'orders_data': orders_data,
        'shipment_data': shipment_data

    }
    return HttpResponse(template.render(context, request))


@login_required
def merchandise(request):
    merchandise_data = Merchandise.objects.all()
    merchandise_data = merchandise_data.order_by('pk')
    template = loader.get_template('merchandise/merchandise.html')
    context = {
        'merchandise_data': merchandise_data
    }
    return HttpResponse(template.render(context, request))


@login_required
def contracts(request):
    contracts_data = Contract.objects.all()
    contracts_data = contracts_data.order_by('pk')
    template = loader.get_template('contract/contracts.html')
    context = {
        'contracts_data': contracts_data
    }
    return HttpResponse(template.render(context, request))


@login_required
def storage(request):
    stock_data = Stock.objects.all()
    stock_data = stock_data.order_by('pk')
    template = loader.get_template('storage/storage.html')
    context = {
        'stock_data': stock_data
    }
    return HttpResponse(template.render(context, request))


@login_required
def supply_orders_for_contract(request, contract_id):
    supply_orders_data = SupplyOrder.objects.filter(contract=get_object_or_404(Contract, pk=contract_id))
    supply_orders_data = supply_orders_data.order_by('pk')
    template = loader.get_template('supply_order/supply_orders.html')
    context = {
        'supply_orders_data': supply_orders_data,
        'contract': get_object_or_404(Contract, pk=contract_id)
    }
    return HttpResponse(template.render(context, request))


@login_required
def supply_orders(request):
    supply_orders_data = SupplyOrder.objects.all()
    supply_orders_data = supply_orders_data.order_by('pk')
    template = loader.get_template('supply_order/supply_orders.html')
    context = {
        'supply_orders_data': supply_orders_data
    }
    return HttpResponse(template.render(context, request))


#
# edit related
#
@login_required
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


@login_required
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


@login_required
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


@login_required
def order_edit(request, order_id):
    order_data = get_object_or_404(Order, pk=order_id)
    client_data = Client.objects.all()
    merch_data = Merchandise.objects.all()
    if request.method == 'POST':
        order_data.client = get_object_or_404(Client, pk=request.POST.get('client_id'))
        order_data.merch = get_object_or_404(Merchandise, pk=request.POST.get('merch_id'))
        order_data.amount = request.POST.get('amount')
        order_data.order_date = request.POST.get('order_date')
        order_data.paid = request.POST.get('order_paid')
        order_data.total = order_data.merch.price * float(order_data.amount)
        order_data.save()
        return HttpResponseRedirect('/orders')
    else:
        template = loader.get_template('order/order_edit.html')
        context = {
            'order_data': order_data,
            'client_data': client_data,
            'merch_data': merch_data,
        }
        return HttpResponse(template.render(context, request))


@login_required
def merchandise_edit(request, merch_id):
    merch_data = get_object_or_404(Merchandise, pk=merch_id)
    manufacturers_data = Manufacturer.objects.all()
    if request.method == 'POST':
        merch_data.name = request.POST.get('name')
        merch_data.price = request.POST.get('price')
        merch_data.description = request.POST.get('description')
        merch_data.manufacturer = get_object_or_404(Manufacturer, pk=request.POST.get('manufacturer'))
        merch_data.save()
        return HttpResponseRedirect('/merchandise')
    else:
        template = loader.get_template('merchandise/merchandise_edit.html')
        context = {
            "manufacturers_data": manufacturers_data,
            'merch_data': merch_data,
        }
        return HttpResponse(template.render(context, request))


@login_required
def stock_edit(request, stock_id):
    stock_data = get_object_or_404(Stock, pk=stock_id)
    if request.method == 'POST':
        stock_data.amount = request.POST.get('amount')
        stock_data.save()
        return HttpResponseRedirect('/storage')
    else:
        template = loader.get_template('storage/stock_edit.html')
        context = {
            "stock_data": stock_data,
        }
        return HttpResponse(template.render(context, request))


@login_required
def contract_edit(request, contract_id):
    contract_data = get_object_or_404(Contract, pk=contract_id)
    if request.method == 'POST':
        contract_data.supplier = get_object_or_404(Supplier, pk=request.POST.get('supplier'))
        contract_data.start_date = request.POST.get('contract_start_date')
        contract_data.conclusion_date = request.POST.get('contract_end_date')
        contract_data.text = request.POST.get('description')
        contract_data.save()
        return HttpResponseRedirect('/contracts')
    else:
        template = loader.get_template('contract/contract_edit.html')
        suppliers_data = Supplier.objects.all()

        context = {
            'suppliers_data': suppliers_data,
            'contract_data': contract_data,
        }
        return HttpResponse(template.render(context, request))


@login_required
def supply_order_edit(request, order_id):
    supply_order_data = get_object_or_404(SupplyOrder, pk=order_id)
    if request.method == 'POST':
        supply_order_data.merch = get_object_or_404(Merchandise, pk=request.POST.get('merch_id'))
        supply_order_data.order_date = request.POST.get('supply_order_start_date')
        supply_order_data.delivery_date = request.POST.get('supply_order_delivery_date')
        supply_order_data.amount = request.POST.get('amount')
        supply_order_data.price = supply_order_data.merch.price
        supply_order_data.save()
        return HttpResponseRedirect('/supply_orders/' + str(supply_order_data.contract.id))
    else:
        template = loader.get_template('supply_order/supply_order_edit.html')
        merch_data = Merchandise.objects.all()
        context = {
            'supply_order_data': supply_order_data,
            'merch_data': merch_data,
        }
        return HttpResponse(template.render(context, request))


#  Add related
#
@login_required
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


@login_required
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


@login_required
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


@login_required
def merchandise_add(request):
    if request.method == 'POST':
        merch_data = Merchandise()
        merch_data.name = request.POST.get('name')
        merch_data.price = request.POST.get('price')
        merch_data.description = request.POST.get('description')
        merch_data.manufacturer = get_object_or_404(Manufacturer, pk=request.POST.get('manufacturer'))
        merch_data.save()
        stock_data = Stock()
        stock_data.merch = merch_data
        stock_data.amount = 0
        stock_data.save()
        return HttpResponseRedirect('/merchandise')
    else:
        template = loader.get_template('merchandise/merchandise_add.html')
        manufacturers_data = Manufacturer.objects.all()
        context = {
            "manufacturers_data": manufacturers_data,
        }
        return HttpResponse(template.render(context, request))


@login_required
def order_add(request):
    if request.method == 'POST':
        order_data = Order()
        order_data.client = get_object_or_404(Client, pk=request.POST.get('client_id'))
        order_data.merch = get_object_or_404(Merchandise, pk=request.POST.get('merch_id'))
        order_data.amount = request.POST.get('amount')
        order_data.order_date = request.POST.get('order_date')
        order_data.paid = False
        order_data.total = order_data.merch.price * float(order_data.amount)
        order_data.save()
        shipment_data = Shipment()
        shipment_data.order = order_data
        shipment_data.status = "Ожидание оплаты"
        shipment_data.save()
        return HttpResponseRedirect('/orders')
    else:
        template = loader.get_template('order/order_add.html')
        client_data = Client.objects.all()
        merch_data = Merchandise.objects.all()
        context = {
            'client_data': client_data,
            'merch_data': merch_data,
        }
        return HttpResponse(template.render(context, request))


@login_required
def contract_add(request):
    if request.method == 'POST':
        contract_data = Contract()
        contract_data.supplier = get_object_or_404(Supplier, pk=request.POST.get('supplier'))
        contract_data.start_date = request.POST.get('contract_start_date')
        contract_data.conclusion_date = request.POST.get('contract_end_date')
        contract_data.text = request.POST.get('description')
        contract_data.save()
        return HttpResponseRedirect('/contracts')
    else:
        template = loader.get_template('contract/contract_add.html')
        suppliers_data = Supplier.objects.all()
        context = {
            'suppliers_data': suppliers_data,
        }
        return HttpResponse(template.render(context, request))


@login_required
def supply_order_add_with_contract(request, contract_id):
    if request.method == 'POST':
        supply_order_data = SupplyOrder()
        supply_order_data.contract = get_object_or_404(Contract, pk=contract_id)
        supply_order_data.merch = get_object_or_404(Merchandise, pk=request.POST.get('merch_id'))
        supply_order_data.order_date = request.POST.get('supply_order_start_date')
        supply_order_data.delivery_date = request.POST.get('supply_order_delivery_date')
        supply_order_data.amount = request.POST.get('amount')
        supply_order_data.shipped = False
        supply_order_data.price = supply_order_data.merch.price
        supply_order_data.save()
        return HttpResponseRedirect('/supply_orders/' + str(supply_order_data.contract.id))
    else:
        template = loader.get_template('supply_order/supply_order_add.html')
        contract_data = get_object_or_404(Contract, pk=contract_id)
        merch_data = Merchandise.objects.all()
        context = {
            'contract_data': contract_data,
            'merch_data': merch_data,
            'specific_contract': True,
        }
        return HttpResponse(template.render(context, request))


@login_required
def supply_order_add(request):
    if request.method == 'POST':
        supply_order_data = SupplyOrder()
        supply_order_data.contract = get_object_or_404(Contract, pk=request.POST.get('contract_id'))
        supply_order_data.merch = get_object_or_404(Merchandise, pk=request.POST.get('merch_id'))
        supply_order_data.order_date = request.POST.get('supply_order_start_date')
        supply_order_data.delivery_date = request.POST.get('supply_order_delivery_date')
        supply_order_data.amount = request.POST.get('amount')
        supply_order_data.shipped = False
        supply_order_data.price = supply_order_data.merch.price
        supply_order_data.save()
        return HttpResponseRedirect('/supply_orders')
    else:
        template = loader.get_template('supply_order/supply_order_add.html')
        contract_data = Contract.objects.all()
        merch_data = Merchandise.objects.all()
        context = {
            'contract_data': contract_data,
            'merch_data': merch_data,
        }
        return HttpResponse(template.render(context, request))


#
# Remove related
#
@login_required
def client_remove(request, client_id):
    try:
        client_data = get_object_or_404(Client, pk=client_id).delete()
    except RestrictedError as e:
        print(e.restricted_objects)
        template = loader.get_template('removal_error.html')
        context = handleRemovalError(e.restricted_objects, get_object_or_404(Client, pk=client_id))
        context['errored_obj_type'] = "Client"
        print(context)
        return HttpResponse(template.render(context, request))

    return HttpResponseRedirect('/clients')


@login_required
def manufacturer_remove(request, manufacturer_id):
    try:
        manufacturer_data = get_object_or_404(Manufacturer, pk=manufacturer_id).delete()
    except RestrictedError as e:
        print(e.restricted_objects)
        template = loader.get_template('removal_error.html')
        context = handleRemovalError(e.restricted_objects, get_object_or_404(Manufacturer, pk=manufacturer_id))
        context['errored_obj_type'] = "Manufacturer"
        print(context)
        return HttpResponse(template.render(context, request))

    return HttpResponseRedirect('/manufacturers')


@login_required
def supplier_remove(request, supplier_id):
    try:
        supplier_data = get_object_or_404(Supplier, pk=supplier_id).delete()
    except RestrictedError as e:
        print(e.restricted_objects)
        template = loader.get_template('removal_error.html')
        context = handleRemovalError(e.restricted_objects, get_object_or_404(Supplier, pk=supplier_id))
        context['errored_obj_type'] = "Supplier"
        print(context)
        return HttpResponse(template.render(context, request))

    return HttpResponseRedirect('/suppliers')


@login_required
def order_remove(request, order_id):
    try:
        order_data = get_object_or_404(Order, pk=order_id).delete()
    except RestrictedError as e:
        print(e.restricted_objects)
        template = loader.get_template('removal_error.html')
        context = handleRemovalError(e.restricted_objects, get_object_or_404(Order, pk=order_id))
        context['errored_obj_type'] = "Order"
        print(context)
        return HttpResponse(template.render(context, request))

    return HttpResponseRedirect('/orders')


@login_required
def merch_remove(request, merch_id):
    try:
        merch_data = get_object_or_404(Merchandise, pk=merch_id).delete()
    except RestrictedError as e:
        print(e.restricted_objects)
        template = loader.get_template('removal_error.html')
        context = handleRemovalError(e.restricted_objects, get_object_or_404(Merchandise, pk=merch_id))
        context['errored_obj_type'] = "Merch"
        print(context)
        return HttpResponse(template.render(context, request))

    return HttpResponseRedirect('/merchandise')


@login_required
def contract_remove(request, contract_id):
    try:
        contract_data = get_object_or_404(Contract, pk=contract_id).delete()
    except RestrictedError as e:
        print(e.restricted_objects)
        template = loader.get_template('removal_error.html')
        context = handleRemovalError(e.restricted_objects, get_object_or_404(Contract, pk=contract_id))
        context['errored_obj_type'] = "Contract"
        print(context)
        return HttpResponse(template.render(context, request))

    return HttpResponseRedirect('/contracts')


@login_required
def supply_order_remove(request, order_id):
    try:
        order_data = get_object_or_404(SupplyOrder, pk=order_id).delete()
    except RestrictedError as e:
        print(e.restricted_objects)
        template = loader.get_template('removal_error.html')
        context = handleRemovalError(e.restricted_objects, get_object_or_404(SupplyOrder, pk=order_id))
        context['errored_obj_type'] = "Supply_order"
        print(context)
        return HttpResponse(template.render(context, request))
    return HttpResponseRedirect('/supply_orders')


@login_required
def supply_order_received(request, order_id):
    order_data = get_object_or_404(SupplyOrder, pk=order_id)
    order_data.shipped = True
    order_data.save()
    storage_data = get_object_or_404(Stock, pk=order_data.merch.id)
    storage_data.amount = storage_data.amount + order_data.amount
    storage_data.save()
    return HttpResponseRedirect('/supply_order/' + str(order_id))


@login_required
def order_paid(request, order_id):
    order_data = get_object_or_404(Order, pk=order_id)
    order_data.paid = True
    order_data.save()
    shipment_data = get_object_or_404(Shipment, pk=order_id)
    shipment_data.status = "Ожидание отгрузки"
    shipment_data.save()
    return HttpResponseRedirect('/order/' + str(order_id))


@login_required
def order_shipped(request, order_id):
    shipment_data = get_object_or_404(Shipment, pk=order_id)

    order_data = get_object_or_404(Order, pk=order_id)
    stock_data = get_object_or_404(Stock, pk=order_data.merch)
    print(stock_data.amount)
    print(order_data.amount)
    if stock_data.amount >= order_data.amount:
        stock_data.amount = stock_data.amount - order_data.amount
        stock_data.save()
        shipment_data.status = "Отгружен"
        shipment_data.save()
        return HttpResponseRedirect('/order/' + str(order_id))
    else:
        return HttpResponse("Так нельзя. Кол-во товара на складе, меньше чем в заказе")

    # AJAX Stuff


def ajax_merchandise_price(request, merchandise_id):
    merch = get_object_or_404(Merchandise, pk=merchandise_id)
    data = {
        'price': merch.price
    }
    return JsonResponse(data)


def ajax_contact_dates(request, contract_id):
    contact = get_object_or_404(Contract, pk=contract_id)
    data = {
        'start': contact.start_date,
        'end': contact.conclusion_date
    }
    return JsonResponse(data)


def handleRemovalError(restricted_objects, errored_obj):
    orders_data = []
    contracts_data = []
    clients_data = []
    manufacturers_data = []
    suppliers_data = []
    merchandise_data = []
    supply_order_data = []
    context = {
        'errored_obj': errored_obj,
    }
    for restricted_object in restricted_objects:
        if isinstance(restricted_object, Order):
            orders_data.append(restricted_object)
        if isinstance(restricted_object, Contract):
            contracts_data.append(restricted_object)
        if isinstance(restricted_object, Client):
            clients_data.append(restricted_object)
        if isinstance(restricted_object, SupplyOrder):
            supply_order_data.append(restricted_object)
        if isinstance(restricted_object, Manufacturer):
            manufacturers_data.append(restricted_object)
        if isinstance(restricted_object, Supplier):
            suppliers_data.append(restricted_object)
        if isinstance(restricted_object, Merchandise):
            merchandise_data.append(restricted_object)
    print(orders_data)
    if len(orders_data) > 1:
        context['orders'] = orders_data
    elif len(orders_data) == 1:
        context['order'] = orders_data[0]

    if len(contracts_data) > 1:
        context['contracts'] = contracts_data
    elif len(contracts_data) == 1:
        context['contract'] = contracts_data[0]

    if len(clients_data) > 1:
        context['clients'] = clients_data
    elif len(clients_data) == 1:
        context['client'] = clients_data[0]

    if len(supply_order_data) > 1:
        context['supply_orders'] = supply_order_data
    elif len(supply_order_data) == 1:
        context['supply_order'] = supply_order_data[0]

    if len(manufacturers_data) > 1:
        context['manufacturers'] = manufacturers_data
    elif len(manufacturers_data) == 1:
        context['manufacturer'] = manufacturers_data[0]

    if len(suppliers_data) > 1:
        context['suppliers'] = suppliers_data
    elif len(suppliers_data) == 1:
        context['supplier'] = suppliers_data[0]

    if len(merchandise_data) > 1:
        context['merchandise'] = merchandise_data
    elif len(merchandise_data) == 1:
        context['merch'] = merchandise_data[0]

    return context
