from django.views.generic import ListView, DetailView, CreateView
from .models import Cheese

class CheeseListView(ListView):
    """Class docstring"""
    model = Cheese


class CheeseDetailView(DetailView):
    """Class docstring"""
    model = Cheese

class CheeseCreateView(CreateView):
    model = Cheese
    fields = ['name', 'description', 'firmness', 'country_of_origin']
    