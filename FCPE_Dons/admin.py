from django.contrib import admin
from .models import Membre,Don

# Register your models here.
class MembreAdmin(admin.ModelAdmin):
   list_display   = ('civilité', 'nom', 'prénom', 'catégorie_membre', str)
   list_filter    = ('civilité','catégorie_membre',)
   ordering       = ('nom', )
   search_fields  = ('nom', 'prénom')

class DonAdmin(admin.ModelAdmin):
   list_display   = ('desciption_du_don','membre','date_du_don','nom_contact')
   list_filter    = ('membre','date_du_don',)
   ordering       = ('desciption_du_don', )
   search_fields  = ('membre','desciption_du_don')

admin.site.register(Membre,MembreAdmin)
admin.site.register(Don,DonAdmin)