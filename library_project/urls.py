"""library_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from django.conf.urls import include, url

from . import hello_resource

#from .hello_resource import _HelloRootView


urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^api/hello', include(hello_resource.urls)),
    #path('api/hello/', hello_resource._HelloRootView, name='hello'),
    #path('api/hello/', _HelloRootView.as_view()),
    path('api/hello/', include('books.urls')),

]

