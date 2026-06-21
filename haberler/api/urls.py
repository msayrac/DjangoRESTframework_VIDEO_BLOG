from django.urls import path
# from haberler.api import views as api_views
from haberler.api.views import MakaleListCreateAPIView,MakaleDetailAPIView,GazeteciListCreateAPIView

urlpatterns = [    
    # path('makaleler/', api_views.makale_list_create_api_view, name='makale-listesi'),
    path('yazarlar/', GazeteciListCreateAPIView.as_view(), name='yazar-listesi'),
    path('makaleler/', MakaleListCreateAPIView.as_view(), name='makale-listesi'),
    path('makaleler/<int:pk>/', MakaleDetailAPIView.as_view(), name='makale-detay'),
    # path('makaleler/<int:pk>/', api_views.makale_detail_api_view, name='makale-detay')
]


