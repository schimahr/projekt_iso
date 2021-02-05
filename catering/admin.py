from django.contrib import admin
from .models import Jelo, Menu, Narudzba

admin.site.register(Jelo)
admin.site.register(Menu)
admin.site.register(Narudzba)

admin.site.site_header="Administracija"
admin.site.index_title="Administaracija catering aplikacije"
# Register your models here.
