from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('check', views.check, name='check'),
    path('Contacts', views.Contacts, name='Contacts'),
    path('News', views.News, name='News'),
    path('Products', views.Products, name='Products'),
    path('Services', views.Services, name='Services'),
    path('scss', views.scss, name='scss'),
    path('api', views.api, name='api')


]
