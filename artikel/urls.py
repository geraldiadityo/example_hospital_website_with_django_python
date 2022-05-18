from django.urls import path, re_path

from .views import (
    ArtikelDetailView,
    ArtikelKategoriListView,
    ArtikelListView,
)

app_name = 'artikel'

urlpatterns = [
    re_path(r'^artikel/kategori/(?P<kategori>[\w]+)/(?P<page>\d+)/$',ArtikelKategoriListView.as_view(),name='kategori'),
    re_path(r'^artikel/detail/(?P<slug>[\w-]+)/$',ArtikelDetailView.as_view(),name='detail'),
    re_path(r'^artikel/(?P<page>\d+)/$',ArtikelListView.as_view(),name='list'),
]
