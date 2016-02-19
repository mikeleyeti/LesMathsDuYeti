from django.db import models


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
    civilité = models.CharField(max_length=1,choices=GENRES,default='H')
    nom = models.CharField(max_length=30,blank=False)
    prénom = models.CharField(max_length=30,blank=False)
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

