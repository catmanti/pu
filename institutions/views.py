from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from .models import Institution
# Create your views here.


class InstitutionsListView(ListView):
    model = Institution
    paginate_by = 6


class InstitutionUpdateView(UpdateView):
    model = Institution
    fields = '__all__'


class InstitutionDetail(DetailView):
    model = Institution
    # fields = '__all__'
