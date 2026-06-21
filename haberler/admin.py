from django.contrib import admin
from haberler.models import Makale, Gazeteci
# Register your models here.


# admin panelini gorunumunu ozellestiren bir sınıf yaz
class MakaleAdmin(admin.ModelAdmin):
    # list_display içinde hangi sütunları görmek istiyorsak isimlerini yazıyoruz
    list_display =('baslik','yazar','sehir','yaratılma_tarihi','yayınlanma_tarihi','aktif')
    
    # İsteğe bağlı: Sağ tarafa yazar veya tarihe göre filtreleme paneli ekler
    list_filter = ('yazar', 'yaratılma_tarihi')
    
    # İsteğe bağlı: Başlık veya yazar içinde arama yapabilen bir arama çubuğu ekler
    search_fields = ('baslik', 'yazar')


class GazeteciAdmin(admin.ModelAdmin):
    list_display = ('isim','soyisim','biyografi')
    list_filter =('isim', 'soyisim')
    search_fields = ('isim', 'soyisim','biyografi')

admin.site.register(Makale, MakaleAdmin)
admin.site.register(Gazeteci,GazeteciAdmin)


