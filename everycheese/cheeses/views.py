from django.views.generic import ListView, DetailView
from .models import Cheese

class CheeseListView(ListView):
    """Class docstring"""
    model = Cheese


class CheeseDetailView(DetailView):
    """Class docstring"""
    model = Cheese
