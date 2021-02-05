from django.urls import path

from .views import HomePageView, RegistracijaView, PregledMenijaView, PregledMenijaDetail, PregledJelaView, PregledJelaDetail
from .views import CreateJeloView, UpdateJeloView, CreateMenuView, UpdateMenuView, CreateNarudzbaView, NarudzbaListView, NarudzbaDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name="index"),
    path('accounts/registracija', RegistracijaView.as_view(), name="registracija"),
    path('meniji', PregledMenijaView.as_view(), name="meniji"),
    path('meniji/<int:pk>/', PregledMenijaDetail.as_view(), name="detaljni_meni"),
    path('jela', PregledJelaView.as_view(), name="jela"),
    path('jela/<int:pk>/', PregledJelaDetail.as_view(), name="detaljno_jelo"),
    path('jela/dodaj_jelo', CreateJeloView.as_view(), name="kreiranje_jela"),
    path('jela/<int:pk>/uredi_jelo', UpdateJeloView.as_view(), name="uredivanje_jela"),
    path('meniji/dodaj_menu', CreateMenuView.as_view(), name="kreiranje_menija"),
    path('meniji/<int:pk>/uredi_menu', UpdateMenuView.as_view(), name="uredivanje_menija"),
    path('naruci', CreateNarudzbaView.as_view(), name="narucivanje"),
    path('narudzbe', NarudzbaListView.as_view(), name="narudzbe"),
    path('narudzbe/<int:pk>/', NarudzbaDetailView.as_view(), name="detaljna_narudzba"),
]