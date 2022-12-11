from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Institution
# Create your views here.


class InstitutionsListView(ListView):
    model = Institution
    paginate_by = 6
