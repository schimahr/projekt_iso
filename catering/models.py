from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

# Create your models here.


class Jelo(models.Model):
    GLAVNO_JELO = 'Glavno jelo'
    PREDJELO = 'Predjelo'
    DEZERT = 'Desert'
    SALATA = 'Salata'
    UMAK = 'Dodatak uz jelo'
    TIPOVI_JELA = [
        (PREDJELO, 'Predjelo'),
        (GLAVNO_JELO,'Glavno jelo'),
        (DEZERT, 'Desert'),
        (SALATA, 'Salata'),
        (UMAK, 'Dodatak uz jelo')
    ]
    naziv_jela = models.CharField(max_length = 50)
    opis_jela = models.CharField(max_length = 200)
    tip_jela = models.CharField(max_length = 20, choices=TIPOVI_JELA)
    cijena = models.IntegerField()

    class Meta:
        verbose_name = "Jelo"
        

    def __str__(self):
        return str(self.naziv_jela)

class Menu(models.Model):
    naziv_menija = models.CharField(max_length = 100)
    jelo_na_meniju = models.ManyToManyField(Jelo, related_name="jela", verbose_name="Jela u meniju")

    def save_model(self, request, obj, form, change):
        return super(Menu, self).save_model(request, obj, form, change)

    class Meta:
        verbose_name = "Meni"
        verbose_name_plural = "Meniji"

    def __str__(self):
        return str(self.naziv_menija)

    @property
    def ukupna_cijena(self):
        return self.jelo_na_meniju.aggregate(total=models.Sum('cijena'))['total']

class Narudzba(models.Model):
    narucitelj = models.ForeignKey(User, on_delete=models.CASCADE)
    adresa = models.CharField(max_length=100)
    datum_usluge = models.DateField()
    kontakt_broj = models.CharField(max_length=15)
    broj_posluzitelja = models.IntegerField()
    odabrani_meni = models.ForeignKey(Menu, on_delete=models.CASCADE)
    kolicina = models.IntegerField()
    napomena = models.TextField()

    class Meta:
        verbose_name_plural = "Narudžbe"


    @property
    def cijena_usluge(self):
        iznos = self.odabrani_meni.ukupna_cijena*self.kolicina
        return iznos