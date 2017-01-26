from django.shortcuts import render, HttpResponse, redirect
from . import models
from models import Courses

def index(request):

    courses = models.Courses.objects.all()
    context = {
        'courses':courses
    }
    return render(request, 'courses/index.html', context)

def add(request):
    n = Courses(name=request.POST['name'], description=request.POST['description'])
    n.save()
    return redirect('/')

def delete(request, id):
    courses = models.Courses.objects.get(id=id)
    context = {
        'name':courses.name,
        'description':courses.description,
        'id':courses.id
    }
    return render(request, 'courses/destroy.html', context)

def destroy(request, id):
    d = models.Courses.objects.get(id=id)
    d.delete()
    return redirect('/')

def users_courses(request):
    courses = Courses.account.all()
    context = {
        'courses':courses
    }
    return render(request, 'courses/u_c.html', context)
