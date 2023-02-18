from django.shortcuts import render,redirect
from .models import tarea
from .forms import TareaForm

# Create your views here.
def home(request):
    tareas=tarea.objects.all()
    context={'tareas':tareas}
    return render(request,'home.html',context)

def agregar(request):
    if request.method == "post":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    context = {'form':form}
    return render(request,'agregar.html',context)

def eliminar(request,tarea_id):
    tarea=tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('home')

def editar(request,tarea_id):
    tarea=tarea.objects.get(id=tarea_id)
    if request.method == "post":
        form = TareaForm(request.POST,instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm(instance=tarea)
    context = {'form':form}
    return render(request,'editar.html',context)