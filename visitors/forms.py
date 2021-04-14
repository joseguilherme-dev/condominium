from django import forms
from visitors.models import Visitor

class VisitorForm(forms.ModelForm):

    class Meta:
        model = Visitor
        fields = ['complete_name','cpf', 'birthday_date', 'house_num', 'vehicle_plate']