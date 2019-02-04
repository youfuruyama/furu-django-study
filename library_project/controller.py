#import responder
from django.urls import path

from . import hello_resource


def create_server():

    api = [
        path('admin/', admin.site.urls),
    ]

    #api = responder.API(cors=True)
    #api = 'http://localhost:8000'

    hello_resource.add_route(api)

    return api
