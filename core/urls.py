from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from prova.views import ClientesViewSet,FiltrarViewSet
from django.conf import settings
from prova.serializers import ClienteSerializer
from prova.serializers import Cliente2Serializer
from django.conf.urls.static import static
router = routers.DefaultRouter()
router.register('MulheresMeeren', ClientesViewSet, basename='Cliente')

router.register('Filtro-Sexo/',FiltrarViewSet, basename='Cliente2')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls), name='index'),
    #path('carga_dados',views.ClientesViewSet.carga_dados, name='carga_dados')
    #path('cliente/<str:nome_arquivo>/carga_dados/', ClienteSerializer.carga_dados,name='carga_dados')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)