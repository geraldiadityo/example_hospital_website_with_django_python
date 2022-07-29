from django.shortcuts import render
from penulis.models import Spesialist,Departement,JadwalDokter
def home(request):
    dokter = Spesialist.objects.all().order_by('-date_created')
    departement = Departement.objects.all().order_by('-date_created')
    departement_list = Departement.objects.values_list('id',flat=True).distinct()
    context = {
        'dokter':dokter,
        'departement':departement,
        'doktercount':dokter.count(),
        'departementcount':departement.count(),
    }
    return render(request, 'dashboard.html',context)
