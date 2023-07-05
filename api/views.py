from django.shortcuts import render
from .models import Lesson
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


def home(request):
    search = request.GET.get("search")
    load = request.GET.get("load_more")
    if search:
        ...
    else:
        search = ""
    lessons = Lesson.objects.all()[::-1][:2]
    if load:
        lessons = Lesson.objects.all()
    if search:
        lessons = Lesson.objects.filter(name__icontains=search)
    
    return render(request, "home.html", {
        "search": search,
        "lessons": lessons
    })

def lesson(request, url):
    lesson = Lesson.objects.all().filter(url=url).first()
    if lesson:
        return render(request, "lesson.html", {
            "lesson": lesson,
        })
    else:
        return render(request, "404.html")