from django.shortcuts import render
from penulis.models import Spesialist,Departement
def home(request):
    dokter = Spesialist.objects.all().order_by('-date_created')
    departement = Departement.objects.all().order_by('-date_created')
    context = {
        'dokter':dokter,
        'departement':departement,
        'doktercount':dokter.count(),
        'departementcount':departement.count(),
    }
    return render(request, 'dashboard.html',context)
