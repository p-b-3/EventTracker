from django.urls import path

from . import views

urlpatterns = [
    path('', views.ConferenceList.as_view(), name="index"),
    path('<int:pk>/',views.ConferenceDetail.as_view(), name='detail'),
    path('about', views.about, name="about")
]
