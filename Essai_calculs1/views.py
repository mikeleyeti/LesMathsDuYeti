from django.shortcuts import render
from sympy import *
from random import randint


# from django.http import HttpResponse


# Create your views here.
def home(request):
    """ Exemple de page HTML, """
    D = randint(1, 6)
    x, y, z = symbols('x y z')
    fact = latex((x + 1) ** D)
    dev = latex(expand((x + 1) ** D))
    derivee = latex(diff(exp(x ** D), x))
    sexe = "Homme"
    couleurs = {'FF0000': 'rouge',
                'ED7F10': 'orange',
                'FFFF00': 'jaune',
                '00FF00': 'vert',
                '0000FF': 'bleu',
                '4B0082': 'indigo',
                '660099': 'violet'}
    return render(request, 'Essai_calculs1/addition.html', locals())
