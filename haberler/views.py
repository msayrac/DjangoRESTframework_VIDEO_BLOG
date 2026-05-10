from django.shortcuts import render
from django.http import HttpResponse

from haberler.models import Makale
# Create your views here.

def getHaber(request):
    # haber = Makale.objects.all()
    # context = {'haber':haber}
    # return render(request, 'home.html', context)
    return HttpResponse("Bu HTTP yazısıdır")