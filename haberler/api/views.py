# haberleri ilgilendiren api buraya yazılacaktır

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from haberler.models import Makale
from haberler.api.serializers import MakaleSerializer

@api_view(['GET', 'POST'])
def makale_list_create_api_view(request):

    if request.method == 'GET':
        makaleler = Makale.objects.filter(aktif=True) # burada nesnelerden olusan query set sorgu kumesi var ama serializer tek bir nesne uzerinden olusuyor
        serializer = MakaleSerializer(makaleler, many=True) # query set veriyoruz hata alacagız
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MakaleSerializer(data=request.data) # dişarıdan gelen data kontrol ediliyor.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)
    

