from django.urls import path
from . import views
from . import hello_resource

urlpatterns = [
    path('', views.index, name='index'),
]

#urlpatterns = [
#    path('', hello_resource._HelloRootView, name='index'),    
#]