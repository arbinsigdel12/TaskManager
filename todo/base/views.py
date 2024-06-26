from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import  *
# Create your views here.


def TodoList(request):
    tasks=Task.objects.all()
    form =TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return  redirect('/')
    context={'tasks':tasks,'form':form}
    return render(request,'base/list.html',context)

def updateTask(request,pk):
  task=Task.objects.get(id=pk)
  form =TaskForm(instance=task)#update garda instance halyo bane tei data placeholder ma auxa
  if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)#yesma instance halena bhane naya form banxa
        if form.is_valid():
            form.save()
            return  redirect('/')
  context={'form':form}
  return render(request,'base/update_task.html',context)


def deleteTask(request,pk):
    item =Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return  redirect('/')
    context= {'item':item}
    return render(request,'base/delete.html',context)