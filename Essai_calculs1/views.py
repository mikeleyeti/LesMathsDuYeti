# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonne ça tue des mouettesssssss en plein vol !</p>"""
    return HttpResponse(text)
