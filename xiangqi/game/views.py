from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse


# Index view - landing page
def index(request):
    return render(request, 'game/index.html')

# Main game view
def game(request, user):
    return HttpResponse('Blank')