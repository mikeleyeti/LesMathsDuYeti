from django.conf.urls import url

from . import views

app_name = 'Maths'

urlpatterns = [
    url(r'^$', views.date_actuelle, name='index')
]