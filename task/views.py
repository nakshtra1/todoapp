from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("description")
        isDone = request.POST.get("is_done")
        if isDone == "on":
            isDone = "True"
        else:
            isDone = "False"
        task = Task(name=title, description=desc, is_done=isDone)
        task.save()
    task = Task.objects.all()
    context = {'task' : task}
    return render(request, 'index.html' , context)
   

def edit(request, task_id):
    # upgrade
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        title = request.POST.get("title")
        desc = request.POST.get("description")
        isDone = request.POST.get("isDone")
        if isDone == "on":
            isDone = "True"
        else:
            isDone = "False"
        task.name = title
        task.description = desc
        task.is_done = isDone
        task.save()
        return redirect('/')

    #render 
    task = Task.objects.get(id=task_id)
    context = {'id' : task.id, 'title' : task.name, 'description' : task.description, 'is_done' : task.is_done}
    return render(request, 'edit.html', context)
    

def delete(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('/')

        #render
    task = Task.objects.get(id=task_id)
    context = {'id' : task.id, 'title' : task.name, 'description' : task.description, 'is_done' : task.is_done}
    return render(request, 'delete.html', context)
    

    