from django.shortcuts import render, redirect
from .models import Bibld
from .forms import BibldForm
from django.views.generic import DetailView, UpdateView, DeleteView


def bibl_book(request):
    bibl = Bibld.objects.order_by('-date_bib')
    return render(request, 'bibl/bibl_book.html', {'bibl': bibl})

class BiblDetailView(DetailView):
    model = Bibld
    template_name = 'bibl/detail_view_bibl.html'
    context_object_name = 'bib'

class BiblUpdateView(UpdateView):
    model = Bibld
    template_name = 'bibl/create_bibl.html'
    form_class = BibldForm

class BiblDeleteView(DeleteView):
    model = Bibld
    success_url = '/bibl/'
    template_name = 'bibl/bibl-delete.html'


def create_bibl(request):
    error = ''
    if request.method == 'POST':
      form = BibldForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('home')

      else:
          error = 'Ошибка!'

    form = BibldForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'bibl/create_bibl.html', data)
