from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
#from django.urls import reverse_lazy
from .models import Order
from django.urls import reverse_lazy




def index(request):
    """
    View function for home page of site.
    """
    return redirect("/orders/")
    # Generate counts of some of the main objects
    pass
class OrderListView(generic.ListView):
    """
    Generic class-based view for a list of books.
    """
    model = Order

class OrderDetailView(generic.DetailView):
    """
    Generic class-based detail view for a book.
    """
    model = Order







class OrderCreate(CreateView):
    model = Order
    fields = '__all__'
    success_url=""
    #initial={'date_of_death':'12/10/2016',}
class OrderUpdate(UpdateView):
    model = Order
    fields = '__all__'
    template_name_suffix = '_update_form'

class OrderDelete(DeleteView):
    model = Order
    success_url =  reverse_lazy('orders')


"""class ClientUpdate(UpdateView):
    model = Client
    fields = "__all__"
class ClientDelete(DeleteView):
    model =Client
    #uccess_url = reverse_lazy('authors')
"""
