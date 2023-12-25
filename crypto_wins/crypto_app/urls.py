from django.urls import path
from . import kayitol, views, anket, girisyap

urlpatterns = [
    path('', views.index, name="index"),
    path('anket', anket.anket, name="anket"),
    path('kayitol', kayitol.kayitol, name="kayitol"),
    path('girisyap', girisyap.girisyap, name="girisyap"),
]
