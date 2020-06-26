from django.conf.urls import url
from DaniProyecto.Apps.AppProyecto.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^cuestionario$', guardarCuestionario, name='guardarCuestionario')
]