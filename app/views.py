from django.shortcuts import render
from .models import simpleModel

from django.views.generic import CreateView, ListView,DetailView,UpdateView,DeleteView

class simpleCreate(CreateView):
    model = simpleModel
    fields = ['title', 'desc']    
    template_name = 'app/create.html'
    success_url = '/list'
    
class simpleListView(ListView):
    model = simpleModel
    template_name = 'app/list.html'
    
class simpleDetailView(DetailView):
    model = simpleModel
    template_name = 'app/detail.html'
    
class simpleUpdateView(UpdateView):
    model = simpleModel
    fields = [
        'title',
        'desc'
    ]
    template_name = 'app/update.html'
    success_url = '/list'
    
class simpleDeleteView(DeleteView):
    model = simpleModel
    template_name = 'app/delete.html'
    success_url = '/list'