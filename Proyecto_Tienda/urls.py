from django.contrib import admin
from django.urls import path,include
from AppTienda.views import cliente, producto, compra

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppTienda/', include('AppTienda.urls')),
]
