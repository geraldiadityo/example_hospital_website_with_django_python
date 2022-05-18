from django import forms
from django.forms import Select, Textarea, TextInput, HiddenInput,FileInput

from .models import Artikel

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = [
            'judul',
            'kategori',
            'penulis',
            'isi',
            'foto',
        ]
        
        labels = {
            'judul':'Judul Artikel',
            'kategori':'Kategori',
            'isi':'Isi Aritkel',
            'foto':'Foto For Artikel',
        }

        widgets = {
            'judul':TextInput,
            'kategori':Select,
            'penulis':HiddenInput(
                attrs={
                    'readonly':'true',
                }
            ),
            'isi':Textarea(
                attrs={
                    'cols':'30',
                    'rows':'4',
                }
            ),
            'foto':FileInput(),
        }
