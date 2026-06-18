from django.contrib import admin
from haberler.models import Makale
# Register your models here.


# admin panelini gorunumunu ozellestiren bir sınıf yaz
class MakaleAdmin(admin.ModelAdmin):
    # list_display içinde hangi sütunları görmek istiyorsak isimlerini yazıyoruz
    list_display =('baslik','yazar','sehir','yaratılma_tarihi','yayınlanma_tarihi','aktif')
    
    # İsteğe bağlı: Sağ tarafa yazar veya tarihe göre filtreleme paneli ekler
    list_filter = ('yazar', 'yaratılma_tarihi')
    
    # İsteğe bağlı: Başlık veya yazar içinde arama yapabilen bir arama çubuğu ekler
    search_fields = ('baslik', 'yazar')


admin.site.register(Makale, MakaleAdmin)



