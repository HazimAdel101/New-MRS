from django.shortcuts import render


def home(request):
    title = 'Home'
    return render(request, "index.html", {"title": title})

