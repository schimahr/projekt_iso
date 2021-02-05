from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Menu, Jelo, Narudzba
from django import forms 
from django.forms.models import inlineformset_factory

class RegistracijaForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","password1","password2"]

    def __init__(self, *args, **kwargs):
        super(RegistracijaForm, self).__init__(*args, **kwargs)

        for fieldname in ["first_name"]:
            self.fields[fieldname].label = "Ime"
        for fieldname in ["last_name"]:
            self.fields[fieldname].label = "Prezime"
        for fieldname in ["username"]:
            self.fields[fieldname].label = "Korisničko ime"
            self.fields[fieldname].help_text = ""
        for fieldname in ["email"]:
            self.fields[fieldname].label = "Email adresa"
        for fieldname in ["password1"]:
            self.fields[fieldname].label = "Lozinka"
        for fieldname in ["password2"]:
            self.fields[fieldname].label = "Potvrdi lozinku"
            self.fields[fieldname].help_text = ""
    
    def save(self, commit=True):
        user = super(RegistracijaForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CreateMenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ['naziv_menija', 'jelo_na_meniju']

    naziv_menija = forms.CharField()

    jelo_na_meniju = forms.ModelMultipleChoiceField(
        queryset = Jelo.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateNarudzbaForm(forms.ModelForm):
    
    class Meta:
        model = Narudzba
        fields = ['adresa','datum_usluge','kontakt_broj','broj_posluzitelja','odabrani_meni','kolicina','napomena']

        widgets = {
            'datum_usluge': DateInput(),
        }