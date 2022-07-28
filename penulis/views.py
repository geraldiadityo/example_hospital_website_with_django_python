from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

from .models import Penulis,Spesialist,Departement,JadwalDokter
from artikel.models import Artikel

from .decorators import (
    unauthentication_user,
    allowed_user,
)

from .forms import (
    PenulisForm,
    UserCreationForm,
    CreateUserForm,
    SpesialistForm,
    DepartementForm,
    JadwalDokterForm,
)

from artikel.forms import ArtikelForm

# Create your views here.
@unauthentication_user
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('penulis:home-penulis')
        else:
            return HttpResponse(
                '<script>alert("username or password incorrect !");window.location="'+str(reverse_lazy('penulis:login'))+'";</script>'
            )
    context = {
        'page_title':'Login Penulis',
    }
    return render(request, 'penulis/login.html',context)

@login_required(login_url='penulis:login')
def logoutView(request):
    logout(request)
    return redirect('penulis:login')


@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['admin','penulis'])
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return HttpResponse(
                '<script>alert("Register for username'+str(username)+'");window.location="'+str(reverse_lazy('penulis:manage-penulis'))+'";</script>'
            )
    
    context = {
        'form':form,
        'page_title':'Register Penulis',
    }
    return render(request, 'penulis/register_penulis.html',context)


@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['admin','penulis'])
def homePenulis(request):
    artikel = request.user.penulis.artikel_set.all().order_by('-published')
    
    context = {
        'page_title':'Artikel Manage Penulis',
        'artikel':artikel,
    }
    
    return render(request, 'penulis/artikel_manage_penulis.html',context)

def artikel_save_form(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            artikels = request.user.penulis.artikel_set.all().order_by('-published')
            data['html_artikel_list'] = render_to_string('penulis/artikel_manage_list_penulis.html',{'artikel':artikels})
        else:
            data['form_is_valid'] = False
    
    context = {
        'form':form,
    }
    data['html_form'] = render_to_string(template_name,context, request=request)
    return JsonResponse(data)

@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['admin','penulis'])
def createArtikel(request):
    penulis = request.user.penulis
    form = ArtikelForm(initial={'penulis':penulis})
    if request.method == 'POST':
        form = ArtikelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(
                '<script>alert("data success sender!");window.location="'+str(reverse_lazy('penulis:home-penulis'))+'";</script>'
            )
    context = {
        'form':form,
        'page_title':'Create Artikel',
    }
    
    return render(request, 'penulis/partartikelcreate.html',context)

@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['admin','penulis'])
def updateArtikel(request,pk):
    artikel = request.user.penulis.artikel_set.get(id=pk)
    form = ArtikelForm(instance=artikel)
    if request.method == 'POST':
        form = ArtikelForm(request.POST,request.FILES,instance=artikel)
        if form.is_valid():
            form.save()
            return HttpResponse(
                '<script>alert("data succes sender!");window.location="'+str(reverse_lazy('penulis:home-penulis'))+'";</script>'
            )
    context = {
        'page_title':'Edit Artikel',
        'form':form,
    }
    return render(request, 'penulis/partartikelupdate.html',context)

@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['admin','penulis'])
def deleteArtikel(request,pk):
    data = dict()
    artikel = request.user.penulis.artikel_set.get(id=pk)
    if request.method == 'POST':
        artikel.delete()
        data['form_is_valid'] = True
        artikels = request.user.penulis.artikel_set.all().order_by('-published')
        data['html_artikel_list'] = render_to_string('penulis/artikel_manage_list_penulis.html',{'artikel':artikels},request=request)
    else:
        context = {
            'artikel':artikel,
        }
        data['html_form'] = render_to_string('penulis/partartikeldelete.html',context,request=request)
    
    return JsonResponse(data)

@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['penulis','admin'])
def managePenulis(request):
    penulis = Penulis.objects.all().order_by('-data_created')
    context = {
        'page_title':'Manage Penulis',
        'penulis':penulis,
    }
    return render(request, 'penulis/manage_penulis.html',context)


@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['admin','penulis'])
def managePublishedartikel(request):
    artikel_unpublished = Artikel.objects.filter(status='unpublished').order_by('-published')
    context = {
        'page_title':'Manage Artikel Unpublished',
        'artikel_unpub':artikel_unpublished,
    }
    
    return render(request, 'penulis/unpublish_manage.html',context)

@login_required(login_url='penulis:login')
def publishedArtikel(request,pk):
    data = dict()
    artikelunpublish = Artikel.objects.get(id=pk)
    if request.method == 'POST':
        artikelunpublish.status = 'published'
        artikelunpublish.save()
        data['form_is_valid'] = True
        artikelunpublish = Artikel.objects.filter(status='unpublished').order_by('-published')
        data['html_unpublish_list'] = render_to_string('penulis/unpublish_manage_list.html',{'artikel_unpub':artikelunpublish},request=request)
    else:
        context = {
            'artikel':artikelunpublish,
        }
        data['html_form'] = render_to_string('penulis/partpublishartikel.html',context, request=request)
    
    return JsonResponse(data)

@login_required(login_url='penulis:login')
def spesialistView(request):
    spesialist = Spesialist.objects.all().order_by('-date_created')
    context = {
        'page_title':'Data Specialist',
        'spesialist':spesialist,
    }
    return render(request, 'penulis/manage_spesialist.html',context)



def saveSpesialist(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            data['form_is_valid'] = True
            form.save()
            listspesialist = Spesialist.objects.all().order_by('-date_created')
            data['html_spesialist_list'] = render_to_string('penulis/manage_spesialist_list.html',{'spesialist':listspesialist})
        else:
            data['form_is_valid'] = False
    
    context = {
        'form':form,
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required(login_url='penulis:login')
def createSpesialist(request):
    if request.method == 'POST':
        form = SpesialistForm(request.POST,request.FILES)
    else:
        form = SpesialistForm()
    
    return saveSpesialist(request, form, 'penulis/partspesialistadd.html')

@login_required(login_url='penulis:login')
def editSpesialist(request,pk):
    spesialist = Spesialist.objects.get(id=pk)
    if request.method == 'POST':
        form = SpesialistForm(request.POST,request.FILES, instance=spesialist)
    else:
        form = SpesialistForm(instance=spesialist)
    
    return saveSpesialist(request, form, 'penulis/partspesialistedit.html')

@login_required(login_url='penulis:login')
def deleteSpesialist(request,pk):
    data = dict()
    spesialist = Spesialist.objects.get(id=pk)
    if request.method == 'POST':
        data['form_is_valid'] = True
        spesialist.delete()
        list_spesialist = Spesialist.objects.all().order_by('-date_created')
        data['html_spesialist_list'] = render_to_string('penulis/manage_spesialist_list.html',{'spesialist':list_spesialist},request=request)
    else:
        context = {
            'spesialist':spesialist,
        }
        data['html_form'] = render_to_string('penulis/partspesialistdelete.html',context,request=request)
    
    return JsonResponse(data)

@login_required(login_url='penulis:login')
def viewDepartement(request):
    departements = Departement.objects.all().order_by('-date_created')
    context = {
        'page_title':'Manage Departement',
        'departement':departements,
    }
    return render(request, 'penulis/manage_departement.html',context)

def save_departement_form(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            data['form_is_valid'] = True
            form.save()
            departements = Departement.objects.all().order_by('-date_created')
            data['html_departement_list'] = render_to_string('penulis/manage_departement_list.html',{'departement':departements})
        else:
            data['form_is_valid'] = False
    
    context = {
        'form':form,
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required(login_url='penulis:login')
def createDepartement(request):
    if request.method == 'POST':
        form = DepartementForm(request.POST)
    else:
        form = DepartementForm()
    
    return save_departement_form(request, form, 'penulis/partdepartementadd.html')

@login_required(login_url='penulis:login')
def editDepartement(request,pk):
    departement = Departement.objects.get(id=pk)
    if request.method == 'POST':
        form = DepartementForm(request.POST, instance=departement)
    else:
        form = DepartementForm(instance=departement)
    
    return save_departement_form(request, form, 'penulis/partdepartementedit.html')

@login_required(login_url='penulis:login')
def deleteDepartment(request,pk):
    data = dict()
    departement = Departement.objects.get(id=pk)
    if request.method == 'POST':
        data['form_is_valid'] = True
        departement.delete()
        departementlist = Departement.objects.all().order_by('-data_created')
        data['html_departement_list'] = render_to_string('penulis/manage_departement_list.html',{'departement':departementlist},request=request)
    else:
        context = {
            'departement':departement,
        }
        data['html_form'] = render_to_string('penulis/partdepartementdelete.html',context,request=request)
    
    return JsonResponse(data)

def save_jadwal_dokter(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            data['form_is_valid'] = True
            form.save()
            jadwal_dokter = JadwalDokter.objects.all()
            data['html_jadwal_list'] = render_to_string('penulis/jadwaldokter_manage_list.html',{'jadwaldokter':jadwal_dokter})
        else:
            data['form_is_valid'] = False
    
    context = {
        'form':form,
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required(login_url='penulis:login')
def createJadwal(request):
    if request.method == 'POST':
        form = JadwalDokterForm(request.POST)
    else:
        form = JadwalDokterForm()
    
    return save_jadwal_dokter(request, form, 'penulis/partjadwaladd.html')

@login_required(login_url='penulis:login')
def editJadwal(request,pk):
    jadwal = JadwalDokter.objects.get(id=pk)
    if request.method == 'POST':
        form = JadwalDokterForm(request.POST,instance=jadwal)
    else:
        form = JadwalDokterForm(instance=jadwal)
    
    return save_jadwal_dokter(request, form, 'penulis/partjadwaledit.html')

@login_required(login_url='penulis:login')
def deleteJadwal(request,pk):
    data = dict()
    jadwal = JadwalDokter.objects.get(id=pk)
    if request.method == 'POST':
        data['form_is_valid'] = True
        jadwal.delete()
        jadwal_list = JadwalDokter.objects.all()
        data['html_jadwal_list'] = render_to_string('penulis/jadwaldokter_manage_list.html',{'jadwaldokter':jadwal_list},request=request)
    else:
        context = {
            'jadwal':jadwal,
        }
        data['html_form'] = render_to_string('penulis/partjadwaldelete.html',context,request=request)
    
    return JsonResponse(data)

@login_required(login_url='penulis:login')
def jadwalManage(request):
    datajadwal = JadwalDokter.objects.all()
    context = {
        'page_title':'Manage Jadwal Dokter',
        'jadwaldokter':datajadwal,
    }
    
    return render(request, 'penulis/jadwaldokter_manage.html',context)
