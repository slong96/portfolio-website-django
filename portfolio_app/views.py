from django.shortcuts import render


def home(request):
    return render(request, 'portfolio_app/home.html', {'title': 'Home'})

def resume(request):
    return render(request, 'portfolio_app/resume.html', {'title': 'Resume'})

def projects(request):
    return render(request, 'portfolio_app/projects.html', {'title': 'Projects'})