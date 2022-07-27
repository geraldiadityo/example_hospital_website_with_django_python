from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Penulis(models.Model):
    user = models.OneToOneField(User, null=True,blank=True ,on_delete = models.CASCADE)
    nama = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=200,null=True)
    profile_pic = models.ImageField(default = 'profile1.png',null=True,blank=True)
    data_created = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return "{}".format(self.nama)

class Spesialist(models.Model):
    nama_spesialist = models.CharField(max_length=100, blank=True,null=True)
    spesialist = models.CharField(max_length=50,blank=True,null=True)
    tentang = models.TextField()
    jadwal = models.DateField(null=True)
    profile_pic = models.ImageField(default='profile1.png', null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.nama_spesialist)


class Departement(models.Model):
    nama_departement = models.CharField(max_length=20, null=True,blank=True)
    keterangan = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{}".format(self.nama_departement)

class JadwalDokter(models.Model):
    dokter = models.ForeignKey(Spesialist, on_delete=models.SET_NULL,null=True)
    senin = models.TextField()
    selasa = models.TextField()
    rabu = models.TextField()
    kamis = models.TextField()
    jumat = models.TextField()
    sabtu = models.TextField()
    
    def __str__(self):
        return "{}".format(self.dokter)
