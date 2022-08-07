from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from penulis.models import Spesialist,Departement,JadwalDokter,ContactPengaduan
def home(request):
    dokter = Spesialist.objects.all().order_by('-date_created')
    departement = Departement.objects.all().order_by('-date_created')
    departement_list = Departement.objects.values_list('id',flat=True).distinct()
    if request.method == 'POST':
        nama = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data_pengaduan = ContactPengaduan.objects.create(nama=nama,email=email,subject=subject,message=message)
        data_pengaduan.save()
        return HttpResponse(
            "<script>alert('Pesan Telah Dikirim!');window.location='"+str(reverse_lazy('dashboard'))+"';</script>"
        )

    context = {
        'dokter':dokter,
        'departement':departement,
        'doktercount':dokter.count(),
        'departementcount':departement.count(),
    }
    return render(request, 'dashboard.html',context)
