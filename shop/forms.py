from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

class CheckoutForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=100)
    prenom = forms.CharField(label='Prénom', max_length=100)
    classe = forms.CharField(label='Classe', max_length=100)
    email = forms.EmailField(label='Email')
    time_slot = forms.ChoiceField(label='Créneau horaire', choices=[
        ('11h15-12h', '11h15-12h'),
        ('12h-13h', '12h-13h'),
        ('13h-14h', '13h-14h')
    ])