"""vhCourseWork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('clients', views.clients, name='Clients'),
    path('manufacturers', views.manufacturers, name='Manufacturers'),
    path('suppliers', views.suppliers, name='Suppliers'),
    path('orders', views.orders, name='Orders'),
    path('contracts', views.contracts, name='Contracts'),
    path('merchandise', views.merchandise, name='Merchandise'),
    path('storage', views.storage, name='Storage'),
    path('supply_orders/<int:contract_id>', views.supply_orders_for_contract, name='Supply orders'),
    path('supply_orders', views.supply_orders, name='Supply orders'),

    path('client/<int:client_id>', views.client, name='Client info'),
    path('manufacturer/<int:manufacturer_id>', views.manufacturer, name='Manufacturer info'),
    path('supplier/<int:supplier_id>', views.supplier, name='Supplier info'),
    path('order/<int:order_id>', views.order, name='Order info'),
    path('stock/<int:stock_id>', views.stock, name='Stock'),
    path('merchandise_info/<int:merch_id>', views.merchandise_info, name='Merchandise info'),
    path('contract/<int:contract_id>', views.contract, name='Contract'),
    path('supply_order/<int:order_id>', views.supply_order, name='Supply order'),

    path('supply_order/<int:order_id>/received', views.supply_order_received, name='Supply order received'),
    path('order/<int:order_id>/paid', views.order_paid, name='Supply order received'),
    path('order/<int:order_id>/shipped', views.order_shipped, name='Supply order received'),

    path('edit/client/<int:client_id>', views.client_edit, name='Client Edit'),
    path('edit/manufacturer/<int:manufacturer_id>', views.manufacturer_edit, name='Manufacturer Edit'),
    path('edit/supplier/<int:supplier_id>', views.supplier_edit, name='Supplier Edit'),
    path('edit/order/<int:order_id>', views.order_edit, name='Order Edit'),
    path('edit/merch/<int:merch_id>', views.merchandise_edit, name='Merchandise Edit'),
    path('edit/stock/<int:stock_id>', views.stock_edit, name='Stock Edit'),
    path('edit/contract/<int:contract_id>', views.contract_edit, name='Contract Edit'),
    path('edit/supply_order/<int:order_id>', views.supply_order_edit, name='Supply order edit'),

    path('remove/client/<int:client_id>', views.client_remove, name='Client Remove'),
    path('remove/manufacturer/<int:manufacturer_id>', views.manufacturer_remove, name='Manufacturer Remove'),
    path('remove/supplier/<int:supplier_id>', views.supplier_remove, name='Supplier Remove'),
    path('remove/order/<int:order_id>', views.order_remove, name='Order Remove'),
    path('remove/merch/<int:merch_id>', views.merch_remove, name='Merch Remove'),
    path('remove/contract/<int:contract_id>', views.contract_remove, name='Contract Remove'),
    path('remove/supply_order/<int:order_id>', views.supply_order_remove, name='Contract Remove'),

    path('add/client', views.client_add, name='Client Add'),
    path('add/manufacturer', views.manufacturer_add, name='Manufacturer Add'),
    path('add/supplier', views.supplier_add, name='Supplier Add'),
    path('add/order', views.order_add, name='Order Add'),
    path('add/merchandise', views.merchandise_add, name='Merchandise Add'),
    path('add/contract', views.contract_add, name='Contract Add'),
    path('add/supply_order/<int:contract_id>', views.supply_order_add_with_contract, name='Supply order add'),
    path('add/supply_order', views.supply_order_add, name='Supply order add'),

    # AJAX related
    # path('ajax/client/<int:client_id>', views.ajax_client, name='Ajax get client'),
    # path('ajax/order/<int:order_id>', views.ajax_order, name='Ajax get order'),
    # path('ajax/contract/<int:contract_id>', views.ajax_contract, name='Ajax get contract'),
    path('ajax/merchandise/price/<int:merchandise_id>', views.ajax_merchandise_price,
         name='Ajax get merchandise price'),
    path('ajax/contract/dates/<int:contract_id>', views.ajax_contact_dates,
         name='Ajax get merchandise price'),
    #  path('ajax/supplier/<int:supplier_id>', views.ajax_supplier, name='Ajax get supplier'),
    # path('ajax/supply_order/<int:supply_order_id>', views.ajax_supply_order, name='Ajax get supply_order'),
    # path('ajax/stock/<int:stock_id>', views.ajax_stock, name='Ajax get stock'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
