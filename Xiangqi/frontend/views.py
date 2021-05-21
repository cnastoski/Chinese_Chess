from django.shortcuts import render

# Create your views here.

#def index(request,  *args, **kwargs):
#    return render(request, 'frontend/index.html')

# Index view - landing page
def index(request):
    return render(request, 'game/index.html')

# Instructions view
def rules(request):
    return render(request, 'game/rules.html')

# Main game view
def play(request):
    return render(request, 'game/play.html')