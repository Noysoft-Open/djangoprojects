from django.shortcuts import render

def home(request):
    context = {
        "home": "Hello World!"
    }
    return render(request, 'blog/index.html', context)

def about(request):
    context = {
        "about": "This is about page"
    }
    return render(request, 'blog/about.html', context)