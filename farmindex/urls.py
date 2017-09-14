from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^datafetch/', views.fetch, name='fetch'),
    url(r'^landlord/', views.landlord, name='landlord'),
    url(r'^household/', views.household, name='household'),
    
    
]
