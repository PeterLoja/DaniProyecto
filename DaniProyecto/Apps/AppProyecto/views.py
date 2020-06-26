from django.shortcuts import render,redirect
from DaniProyecto.Apps.AppProyecto.forms import *
from DaniProyecto.Apps.AppProyecto.models import *


# Create your views here.

def index(request):
    return render(request,'index.html')

def guardarCuestionario(request):
    if request.method == 'POST':
       form_cuestionario=CuestionarioForm(request.POST)
       if form_cuestionario.is_valid():
           cuestionario=form_cuestionario.save(commit=False)
           cuestionario.nombre=request.POST['nombre']
           cuestionario.pregunta1=request.POST['p1']
           cuestionario.pregunta2=request.POST['p2']
           cuestionario.pregunta3 = request.POST['p3']
           cuestionario.pregunta4 = request.POST['p4']
           cuestionario.pregunta5 = request.POST['p5']
           cuestionario.pregunta6 = request.POST['p6']
           cuestionario.pregunta7 = request.POST['p7']
           cuestionario.pregunta8 = request.POST['p8']
           cuestionario.save()
           return redirect('appproyecto:index')
    else:
           form_cuestionario=CuestionarioForm()
    return render(request,'AppProyecto/test.html')