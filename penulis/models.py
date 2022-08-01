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

class Departement(models.Model):
    nama_departement = models.CharField(max_length=20, null=True,blank=True)
    keterangan = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{}".format(self.nama_departement)

class Spesialist(models.Model):
    nama_spesialist = models.CharField(max_length=100, blank=True,null=True)
    spesialist = models.ForeignKey(Departement, on_delete=models.SET_NULL,null=True)
    tentang = models.TextField()
    jadwal = models.DateField(null=True)
    profile_pic = models.ImageField(default='profile1.png', null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.nama_spesialist)
class JadwalDokter(models.Model):
    JADWAL_NORMAL = (
        ('08:30 - 14:15','08:30 - 14:15'),
        ('Kosong','Kosong'),
        ('Cuti','Cuti'),

    )

    JADWAL_JUMAT = (
        ('08:00 - 11:45','08:00 - 11:45'),
        ('Kosong','Kosong'),
        ('Cuti','Cuti'),
    )

    dokter = models.ForeignKey(Spesialist, on_delete=models.SET_NULL,null=True)
    senin = models.TextField(choices=JADWAL_NORMAL)
    selasa = models.TextField(choices=JADWAL_NORMAL)
    rabu = models.TextField(choices=JADWAL_NORMAL)
    kamis = models.TextField(choices=JADWAL_NORMAL)
    jumat = models.TextField(choices=JADWAL_JUMAT)
    sabtu = models.TextField(choices=JADWAL_NORMAL)
    
    def __str__(self):
        return "{}".format(self.dokter)
