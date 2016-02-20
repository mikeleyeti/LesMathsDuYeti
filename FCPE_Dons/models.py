from django.db import models
from django.core.validators import MaxValueValidator
import datetime


# Create your models here.
class Membre(models.Model):
    """
    Classe permettant de lister tous les membres de l'APE.
    """
    GENRES = (
        ('H', 'Monsieur'),
        ('F', 'Madame'),
        ('f', 'Mademoiselle'),
    )
    civilité = models.CharField(max_length=1, choices=GENRES, default='H')
    nom = models.CharField(max_length=30, blank=False)
    prénom = models.CharField(max_length=30, blank=False)
    CATEGORIES_MEMBRES = (
        ('P', "Président de l'A.P.E de Chaingy"),
        ('V', "Vice-Président de l'A.P.E de Chaingy"),
        ('S', "Secrétaire de l'A.P.E de Chaingy"),
        ('M', "Membre de l'A.P.E de Chaingy"),
    )
    catégorie_membre = models.CharField(max_length=1,choices=CATEGORIES_MEMBRES,default='M')
    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return "{} {} {} - {}".format(self.get_civilité_display() ,self.prénom.capitalize(),self.nom.upper(),self.get_catégorie_membre_display())

class Don(models.Model):
    """
    Classe définissant le don
    """
    desciption_du_don = models.CharField(max_length=500, blank=False,verbose_name="Description du don")
    membre = models.ForeignKey('Membre')
    date_du_don = models.DateField(auto_now=True)
    TYPES_DONNATEURS = (
        ('E', "Entreprise"),
        ('P', "Particulier"),
    )
    type_donnateur = models.CharField(max_length=1,choices=TYPES_DONNATEURS,default='E')
    nom_entreprise = models.CharField(max_length=50, blank=True,verbose_name="Nom de l'entreprise (facultatif)")
    nom_contact = models.CharField(max_length=50, blank=False,verbose_name='Nom du contact')
    rue_du_contact = models.CharField(max_length=300, blank=False,verbose_name='Rue')
    cp_du_contact = models.PositiveIntegerField(validators=[MaxValueValidator(99999)], blank=False,verbose_name='Code Postal')
    ville_contact = models.CharField(max_length=50, blank=False,verbose_name='Ville')
    tel_du_contact = models.CharField(max_length=20, blank=True,verbose_name='Téléphone du contact (Facultatif)')
    email_du_contact = models.EmailField(max_length=254, blank=True,verbose_name='E-mail du contact (Facultatif)')
    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.desciption_du_don


