from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cheese

class CheeseListView(ListView):
    """Class docstring"""
    model = Cheese


class CheeseDetailView(DetailView):
    """Class docstring"""
    model = Cheese

class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = ['name', 'description', 'firmness', 'country_of_origin']
    