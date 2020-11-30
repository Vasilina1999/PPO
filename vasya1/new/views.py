from django.shortcuts import render, redirect
from .models import Shopd
from .forms import ShopdForm
from django.views.generic import DetailView, UpdateView, DeleteView


def new_home(request):
    new = Shopd.objects.order_by('-date')
    return render(request, 'new/new_home.html', {'new': new})

class NewDetailView(DetailView):
    model = Shopd
    template_name = 'new/detail_view.html'
    context_object_name = 'shop'

class NewUpdateView(UpdateView):
    model = Shopd
    template_name = 'new/create.html'
    form_class = ShopdForm

class NewDeleteView(DeleteView):
    model = Shopd
    success_url = '/new/'
    template_name = 'new/new-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
      form = ShopdForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('home')

      else:
          error = 'Ошибка!'

    form = ShopdForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'new/create.html', data)