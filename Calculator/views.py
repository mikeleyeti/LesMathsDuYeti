from django.http import HttpResponse


def index(request):
    return HttpResponse("Voici la page d'accueil du Calculator !")
