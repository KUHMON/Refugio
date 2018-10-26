from django.urls import path
from apps.mascota.views import index, mascota_view, mascota_list ,mascota_edit, mascota_delete
from django.conf.urls import url, include

urlpatterns = [
#    path('', index),
#    path('nuevo',mascota_view),
    url(r'^$',index,name='mascota_index'),
    url(r'^nuevo$',mascota_view,name='mascota_crear'),
    url(r'^listar$',mascota_list,name='mascota_listar'),
#    url(r'^listar$',MascotaList.as_view(),name='mascota_listar'),# utilizando clases para las vistas
    url(r'^editar/(?P<id_mascota>\d+)/$',mascota_edit,name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete,name='mascota_eliminar'),
]
