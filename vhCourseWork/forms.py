from django import forms


class ClientForm(forms.Form):
    name = forms.CharField(label="Наименование", required=True, max_length="60")
    first_name = forms.CharField(label="Имя", required=True, max_length="30")
    second_name = forms.CharField(label="Фамилия", required=True, max_length="30")
    third_name = forms.CharField(label="Отчество", required=True, max_length="30")
    address = forms.CharField(label="Адрес", required=True, max_length="150")
    phone = forms.CharField(label="Адрес", required=True, max_length="14")
    tin = forms.CharField(label="ИНН", required=True, max_length="14")
    bank_details = forms.Textarea()
    notes = forms.Textarea()
