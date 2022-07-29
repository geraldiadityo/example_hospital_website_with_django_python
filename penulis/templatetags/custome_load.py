from django import template
from penulis.models import JadwalDokter
register = template.Library()
@register.inclusion_tag('penulis/datajadwal.html')
def loadFromSpesialist(spesialist):
    data = JadwalDokter.objects.filter(dokter__spesialist=spesialist)
    return {'datajadwal':data}

