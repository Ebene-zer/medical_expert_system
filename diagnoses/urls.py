from django.urls import path
from .views import diagnose_view

app_name = 'diagnoses'

urlpatterns = [
    path('', diagnose_view, name='index'),
]
