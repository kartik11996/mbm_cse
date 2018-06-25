from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Publication


class IndexView(generic.ListView):
    template_name = 'publications/index.html'

    def get_queryset(self):
        return Publication.objects.all()


class DetailView(generic.DetailView):
    model = Publication
    template_name = 'publications/detail.html'


class PublicationCreate(CreateView):
    model = Publication
    template_name = 'publications/publication_form.html'
    fields = ['title', 'publisher_name', 'editorial_name', 'year', 'volume', 'doi', 'isbn', 'description', 'edition', 'pages', 'date_of_addition', 'language', 'abstract', 'featured', 'type']


class PublicationUpdate(UpdateView):
    model = Publication
    fields = ['title', 'publisher_name', 'editorial_name', 'year', 'volume', 'doi', 'isbn', 'description', 'edition', 'pages', 'date_of_addition', 'language', 'abstract', 'featured', 'type']


class PublicationDelete(DeleteView):
    model = Publication
    success_url = reverse_lazy('publications:index')


