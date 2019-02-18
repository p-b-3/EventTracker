from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sponsors/sponsors.html')

def sponsor(request):
    return render(request, 'sponsors/sponsor.html')

def search(request):
    return render(request, 'sponsors/search.html')
