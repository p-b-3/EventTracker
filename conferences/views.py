from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Event

class ConferenceList(ListView):
    queryset = Event.objects.order_by('start_date')
#
# def conference(request):
#     return render(request, 'conferences/conference.html')
#
# def search(request):
#     return render(request, 'conferences/search.html')

class ConferenceDetail(DetailView):
    model = Event





def about(request):
    return render(request, 'conferences/about.html')
