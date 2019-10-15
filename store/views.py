from django.shortcuts import render

from store.models import Book


def index(request):
    return render(request, "template.html")


def store(request):
    count = Book.objects.all().count()
    request.session ['location'] = "unknown"
    if request.user.is_authenticated():
        request.session['location'] = "Earth"
    context = {
        'count': count,
    }
    return render(request, 'base.html', context)