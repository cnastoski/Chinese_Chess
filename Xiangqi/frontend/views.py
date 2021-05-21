from django.shortcuts import render

# Create your views here.

# Index view - landing page
def index(request):
    return render(request, 'frontend/index.html')

# Instructions view
def rules(request):
    return render(request, 'frontend/rules.html')

# Main game view
def play(request):
    return render(request, 'frontend/play.html')