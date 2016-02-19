from datetime import datetime
from django.shortcuts import render
from random import randint
from sympy import *


# Create your views here.
def date_actuelle(request):
    return render(request, 'Maths/date.html', {'date': datetime.now()})


def alea(request):
    dé = randint(1,6)
    x = Symbol('x')
    expression_de_départ=latex((x+1)**dé)
    résultat=latex(expand((x+1)**dé))
    return render(request, 'Maths/alea.html', locals())
