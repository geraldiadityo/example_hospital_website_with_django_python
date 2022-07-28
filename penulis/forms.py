from django import forms
from django.forms import TextInput,PasswordInput,Textarea,DateInput,Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Penulis,Spesialist,Departement,JadwalDokter

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'email':'Email'
        }

class PenulisForm(forms.ModelForm):
    class Meta:
        model = Penulis
        fields = '__all__'
        exclude = ['user']

class SpesialistForm(forms.ModelForm):
    class Meta:
        model = Spesialist
        fields = [
            'nama_spesialist',
            'spesialist',
            'tentang',
            'jadwal',
            'profile_pic',
        ]
        
        labels = {
            'nama_spesialist':'Nama Spesialist',
            'spesialist':'Bidang Spesialist',
            'tentang':'Tentang Spesialist',
            'jadwal':'Jadwal Dokter',
            'profile_pic':'Photo',
        }
        
        widgets = {
            'nama_spesialist':TextInput(),
            'spesialist':Select(),
            'tentang':Textarea(
                attrs={
                    'cols':'30',
                    'rows':'4',
                }
            ),
            'jadwal':DateInput(
                attrs={
                    'type':'date',
                }
            ),
        }

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = [
            'nama_departement',
            'keterangan',
        ]
        
        labels = {
            'nama_departement':'Nama Department',
            'keterangan':'Keterangan Departement',
        }

        widgets = {
            'nama_department':TextInput(),
            'Keterangan':Textarea(
                attrs={
                    'cols':'30',
                    'rows':'4',
                }
            ),
        }

class JadwalDokterForm(forms.ModelForm):
    class Meta:
        model = JadwalDokter
        fields = [
            'dokter',
            'senin',
            'selasa',
            'rabu',
            'kamis',
            'jumat',
            'sabtu',
        ]
        
        labels = {
            'dokter':'Nama Dokter',
            'senin':'Jadwal Senen',
            'selasa':'Jadwal Selasa',
            'rabu':'Jadwal Rabu',
            'kamis':'Jadwal Kamis',
            'jumat':'Jadwal Jumat',
            'sabtu':'Jadwal Sabtu',
        }

        widgets = {
            'dokter':Select,
            'senin':TextInput,
            'selasa':TextInput,
            'rabu':TextInput,
            'kamis':TextInput,
            'jumat':TextInput,
            'sabtu':TextInput,
        }
