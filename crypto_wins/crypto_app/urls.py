from django.urls import path
from . import kayitol, views, anket,piyasalar,hakkimizda,sss
urlpatterns = [
    path('', views.index, name="index"),
    path('anket', anket.anket, name="anket"),
    path('kayitol', kayitol.kayitol, name="kayitol"),
    path('piyasalar', piyasalar.piyasalar, name="piyasalar"),
    path('hakkimizda', hakkimizda.hakkimizda, name="hakkimizda"),
    path('sss', sss.sss, name="sss"),
]
