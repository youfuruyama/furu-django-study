import responder

from . import hello_resource

def serve(port):
    create_server().run(address='0.0.0.0', port=port)

def create_server():
    api = responder.API(cors=True)

    hello_resource.add_route(api)

    return api
