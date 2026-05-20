from django.contrib import admin
from haberler.models import Makale, Gazeteci
# Register your models here.


class MakaleAdmin(admin.ModelAdmin):
    #Tablo sutunlarını yazıayoruz
    list_display = ('yazar','baslik','sehir','yayinlanma_tarihi','aktif','yaratilma_tarihi','guncellenme_tarihi')

    list_filter = ('baslik','aciklama','yazar','sehir')

class GazeteciAdmin(admin.ModelAdmin):
    #Tablo sutunlarını yazıayoruz
    list_display = ('isim','soyisim','biyografi')

    list_filter = ('isim','soyisim')

admin.site.register(Makale,MakaleAdmin)
admin.site.register(Gazeteci,GazeteciAdmin)
