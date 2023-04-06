"""Docstring to go over tests."""
from django.http import HttpResponse


def index(request):
    """Docstring to go over tests."""
    return HttpResponse('У меня получилось!')


def second_page(request):
    """Docstring to go over tests."""
    return HttpResponse('А это вторая страница')
