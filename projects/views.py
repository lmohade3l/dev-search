from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects' : projects}
    return render(request , 'projects/projects.html' , context)


def project(request, pk):
    pro = Project.objects.get(id=pk)
    return render(request , 'projects/single-project.html', {'project' : pro} )


def create_project(request) :
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form' : form}
    return render(request , 'projects/project_form.html' , context)


def update_project(request, pk) :
    editing_project = Project.objects.get(id=pk)
    form = ProjectForm(instance= editing_project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=editing_project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form' : form}
    return render(request , 'projects/project_form.html' , context)


def delete_project(request , pk) :
    deleting_project = Project.objects.get(id=pk)
    
    if request.method == 'POST':
        deleting_project.delete()
        return redirect('projects')
    
    context = {'object':deleting_project}
    return render(request , 'projects/delete.html' , context)
