
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='dashboard'),
    path('artikel/',include('artikel.urls',namespace='artikel')),
    path('penulis/',include('penulis.urls',namespace='penulis')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

