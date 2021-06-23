from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=60)
    director = models.CharField(max_length=90)
    phone = models.CharField(max_length=17)
    bank_details = models.CharField(max_length=250)
    tin = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    notes = models.CharField(max_length=255)


class Manufacturer(models.Model):
    name = models.CharField(max_length=60)
    director = models.CharField(max_length=80)
    accountant = models.CharField(max_length=80, null=True)
    phone = models.CharField(max_length=17)
    fax = models.CharField(max_length=17, null=True)
    tin = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    bank_details = models.CharField(max_length=250)
    notes = models.CharField(max_length=255, null=True)


class Merchandise(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.RESTRICT, null=True)


class Stock(models.Model):
    merch = models.OneToOneField(Merchandise, on_delete=models.CASCADE, primary_key=True)
    amount = models.IntegerField()


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, null=True)
    merch = models.ForeignKey(Merchandise, on_delete=models.RESTRICT, null=True)
    amount = models.IntegerField()
    paid = models.BooleanField()
    total = models.FloatField()
    order_date = models.DateField()


class Shipment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    shipped = models.BooleanField
    status = models.CharField(max_length=50)


class Supplier(models.Model):
    name = models.CharField(max_length=80)
    director = models.CharField(max_length=80)
    accountant = models.CharField(max_length=80, null=True)
    phone = models.CharField(max_length=17)
    fax = models.CharField(max_length=17, null=True)
    tin = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    bank_details = models.CharField(max_length=250)
    notes = models.CharField(max_length=255, null=True)


class Contract(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT, null=True)
    text = models.TextField()
    start_date = models.DateField()
    conclusion_date = models.DateField()


class SupplyOrder(models.Model):
    merch = models.ForeignKey(Merchandise, on_delete=models.RESTRICT, null=True)
    contract = models.ForeignKey(Contract, on_delete=models.RESTRICT, null=True)
    amount = models.IntegerField()
    price = models.FloatField()
    shipped = models.BooleanField()
    delivery_date = models.DateField()
