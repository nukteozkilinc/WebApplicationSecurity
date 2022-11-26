# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect,redirect
from .models import Task, Day
import datetime
from .filter import TaskFilter
from .forms import TaskForm


@login_required(login_url="/login/")
def index(request):
    
    context = {'segment': 'index'}
    context["dataset"] = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error ", form.errors)
    context["form"] = TaskForm()
    
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request,))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    

@login_required(login_url="/login/")
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error ", form.errors)
    form = TaskForm()
    return render(request, 'home/new-task.html', {'form':form})

@login_required(login_url="/login/")
def list_view(request):
    context ={}
    context["dataset"] = Task.objects.all()
         
    return render(request, "home/task-list.html", context)
   


@login_required(login_url="/login/")
def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')

@login_required(login_url="/login/")
def edit(request, id):
    context ={}
    obj = get_object_or_404(Task, id = id)

    form = TaskForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "home/edit-task.html", context)

@login_required(login_url="/login/")
def detail_view(request, id):
    context ={}
    context["task"] = Task.objects.get(id = id)
          
    return render(request, "home/detail-task.html", context)

@login_required(login_url="/login/")
def task_done(request, id):
    task = get_object_or_404(Task, id=id)  
    if request.method == 'POST':       
        task.completed = True
        task.save(update_fields=["completed"])
        return redirect('/')     

@login_required(login_url="/login/")
def searchBar(request):
    if request.method == 'GET':
        searched = request.GET.get('searched')
        if searched:
            task = Task.objects.filter(title__contains=searched) 
            return render(request, 'home/searchbar.html', {'task':task, 'searched':searched})
        else:
            print("No information to show")
            return render(request, 'home/searchbar.html', {})