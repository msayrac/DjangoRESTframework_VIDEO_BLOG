from rest_framework import serializers
from haberler.models import Makale, Gazeteci

from datetime import datetime
from datetime import date
from django.utils.timesince import timesince


class MakaleSerializer(serializers.ModelSerializer):

    time_since_pub = serializers.SerializerMethodField()
    # yazar = GazeteciSerializer()
    class Meta:
        model = Makale
        fields = '__all__'
        # fields = ['yazar', 'baslik', 'metin']
        # exclude = ['yazar','baslik','metin']
        read_only_fields = ['id','yaratilma_tarihi','guncellenme_tarihi']


    def get_time_since_pub(self, object):
        time_now = datetime.now()
        pub_date = object.yayinlanma_tarihi
        if object.aktif == True: 
            time_delta = timesince(pub_date,time_now)
            return time_delta
        else:
            return 'Aktif Degil'

    def validate_yayinlanma_tarihi(self, tarih_degeri):
        today = date.today()

        if tarih_degeri > today:
            raise serializers.ValidationError('Yayinlanma tarihi ileri bir tarih olamaz!')
        return tarih_degeri



# standart Serializer
class MakaleDefaultSerializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayinlanma_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    guncellenme_tarihi = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print("validated_data : ", validated_data)
        return Makale.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslik', instance.baslik)
        instance.aciklama = validated_data.get('aciklama', instance.aciklama)
        instance.metin = validated_data.get('metin', instance.metin)
        instance.sehir = validated_data.get('sehir', instance.sehir)
        instance.yayinlanma_tarihi = validated_data.get('yayinlanma_tarihi', instance.yayinlanma_tarihi)
        instance.aktif = validated_data.get('aktif', instance.aktif)

        instance.save()
        return instance
    
    def validate(self, data):
        if data['baslik'] == data['aciklama']:
            raise serializers.ValidationError('Başlık ve acıklama alanları aynı olamaz. Lutfen farklı bir veri giriniz')
        return data
    
    def validate_baslik(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(f'Minumum başlık alanı 20 karakter olmalıdır. Siz -{len(value)}- karakter girdiniz')
        return value

        

class GazeteciSerializer(serializers.ModelSerializer):
    # makaleler = MakaleSerializer(many=True, read_only=True)

    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name ='makale-detay',
    )

    class Meta:
        model = Gazeteci
        fields = '__all__'
