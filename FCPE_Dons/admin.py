from django.contrib import admin
from .models import Membre

# Register your models here.
class MembreAdmin(admin.ModelAdmin):
   list_display   = ('civilité', 'nom', 'prénom', 'catégorie_membre', str)
   list_filter    = ('civilité','catégorie_membre',)
   ordering       = ('nom', )
   search_fields  = ('nom', 'prénom')

admin.site.register(Membre,MembreAdmin)