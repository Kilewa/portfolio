from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'portfolior/home.html')


def projects(request):
    return render(request, 'portfolior/projects.html')