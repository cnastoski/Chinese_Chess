from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Index view - landing page
def index(request):
    return render(request, 'game/index.html')

# Instructions view
def rules(request):
    return render(request, 'game/rules.html')

# Main game view
def game(request, user):
    return HttpResponse('Blank')