from django.contrib import admin

from .models import *

admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Order)
admin.site.register(Manufacturer)
admin.site.register(Stock)
admin.site.register(Supplier)
admin.site.register(SupplyOrder)
admin.site.register(Shipment)
