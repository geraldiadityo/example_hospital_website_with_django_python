from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView

from penulis.models import Penulis
from .models import Artikel
# Create your views here.
class ArtikelPerkategori():
    model = Artikel
    
    def get_last_artikel_each_kategori(self):
        kategorilist = self.model.objects.values_list('kategori',flat=True).distinct()
        queryset = []
        for i in kategorilist:
            artikel = self.model.objects.filter(kategori=i).filter(status='published').latest('-published')
            queryset.append(artikel)
        
        return queryset

class BlogHomeView(TemplateView,ArtikelPerkategori):
    template_name = 'artikel/home.html'
    
    def get_context_data(self):
        data = self.get_last_artikel_each_kategori()
        context = {
            'page_title':'Artikel Home',
            'datakategori':data,
        }
        return context

class ArtikelListView(ListView):
    model = Artikel
    template_name = 'artikel/artikel_list.html'
    context_object_name = 'artikel'
    ordering = ['-published']
    paginate_by = 4

    def get_queryset(self):
        self.queryset = self.model.objects.filter(status='published')
        return super().get_queryset()

    def get_context_data(self,*args,**kwargs):
        kategorilist = self.model.objects.values_list('kategori',flat=True).distinct()
        last_artikel = self.model.objects.filter(status='published').latest('published')
        data_context = {
            'page_title':'Aritkel',
            'kategorilist':kategorilist,
            'lastartikel':last_artikel,
        }
        self.kwargs.update(data_context)
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)

class ArtikelKategoriListView(ListView):
    model = Artikel
    template_name = 'artikel/artikel_kategori_list.html'
    context_object_name = 'artikel'
    ordering = ['-published']
    paginate_by = 4

    def get_queryset(self):
        self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori']).filter(status='published')
        return super().get_queryset()
    
    def get_context_data(self, *args, **kwargs):
        lastartikel = self.model.objects.all().latest('-published')
        kategorilist = self.model.objects.values_list('kategori',flat=True).distinct()
        data_context = {
            'page_title':self.kwargs['kategori'],
            'kategorilist':kategorilist,
            'lastartikel':lastartikel,
        }
        self.kwargs.update(data_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = 'artikel/artikel_detail.html'
    context_object_name = 'artikel'

    def get_context_data(self,*args,**kwargs):
        kategorilist = self.model.objects.values_list('kategori',flat=True).distinct()
        data_context = {
            'page_artikel':'Detail Arikel',
            'kategorilist':kategorilist,
        }
        self.kwargs.update(data_context)
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)

