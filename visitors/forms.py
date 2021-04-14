from django import forms
from visitors.models import Visitor

class VisitorForm(forms.ModelForm):

    class Meta:
        model = Visitor
        fields = ['complete_name','cpf', 'birthday_date', 'house_num', 'vehicle_plate']

        error_messages = {
            'complete_name' : {
                'required' : 'O nome completo do visitante é obrigatório para o registro.'
            },
            'cpf' : {
                'required' : 'O CPF do visitante é obrigatório para o registro.'
            },
            'birthday_date' : {
                'required' : 'A data de nascimento do visitante é obrigatória para o registro.',
                'invalid' : 'A data de nascimento do visitante deve ser informada no formato: DD/MM/AAAA'
            },
            'house_num' : {
                'required' : 'O número da casa que será visitada é obrigatório para o registro.'
            },
        }