from django.urls import path

from . import views

app_name = 'cal'

urlpatterns = [
    # ex: /polls/
    path('', views.home, name='home'),
]