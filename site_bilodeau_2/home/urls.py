from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home-home'),
    path('infolettre/inscription/', views.infolettre_inscription, name='home-infolettre_inscription'),
    #path('infolettre/', views.infol, name='home-redirection'),
    #path('r/<page_de_redirection>/', views.redirection, name='home-redirection'),
]
