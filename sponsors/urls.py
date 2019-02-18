from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="sponsors"),
    path('<int:sponsor_id>', views.sponsor, name="sponsor"),
    path('search', views.search, name="search")
]
