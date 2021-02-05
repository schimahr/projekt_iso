from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django import template
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db import IntegrityError, transaction
from .forms import RegistracijaForm, CreateMenuForm, CreateNarudzbaForm
from .models import Menu, Jelo, Narudzba



# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class RegistracijaView(FormView):
    template_name = 'registracija.html'
    form_class = RegistracijaForm
    success_url = '/'

    def form_valid(self, form):
        obj = form.save()
        return super().form_valid(form)


class PregledMenijaView(ListView):
    model = Menu
    template_name = 'pregled_menija.html'


class PregledMenijaDetail(DetailView):
    model = Menu
    template_name = 'meniji_detail.html'

class PregledJelaView(ListView):
    model = Jelo
    template_name = 'pregled_jela.html'

class PregledJelaDetail(DetailView):
    model = Jelo
    template_name = 'jela_detail.html'

class CreateJeloView(CreateView):
    model = Jelo
    template_name = 'dodaj_jelo.html'
    fields = "__all__"
    success_url = reverse_lazy('index')

class UpdateJeloView(UpdateView):
    model = Jelo
    template_name = 'uredi_jelo.html'
    fields = "__all__"
    success_url = reverse_lazy('index')

class CreateMenuView(CreateView):
    model = Menu
    template_name = 'dodaj_menu.html'
    form_class = CreateMenuForm
    success_url = reverse_lazy('index')

class UpdateMenuView(UpdateView):
    model = Menu
    template_name = 'uredi_menu.html'
    form_class = CreateMenuForm
    success_url = reverse_lazy('index')

class CreateNarudzbaView(CreateView):
    model = Narudzba
    template_name = 'kreiraj_narudzbu.html'
    form_class = CreateNarudzbaForm
    success_url = reverse_lazy('index')

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.narucitelj = self.request.user
        try:
            obj.save()
        except IntegrityError:
            return HttpResponse("Ne radi")
        return HttpResponseRedirect(reverse_lazy('index'))

class NarudzbaListView(ListView):
    model = Narudzba
    template_name = 'pregled_narudzbi.html'

class NarudzbaDetailView(DetailView):
    model = Narudzba
    template_name = 'narudzba_detail.html'