#import responder.status_codes as status_codes
from django.http import HttpResponse

#from .views import respond


#def add_route(api):
    #edge_svc = services.get('hello')
    #if edge_svc is None:
    #    return

#    api.add_route('/api/hello', _HelloRootView())

# -----------------------------------------------------------------------------
# ビュー
# -----------------------------------------------------------------------------

#class _HelloRootView:
#    def __init__(self):
#        self.hello_svc = ""

#    @respond
#    def on_get(self, req, resp):
#        content = [{"msg": "Hello World!"}]
        #return (status_codes.HTTP_200, content)
#        return (HttpResponse(status=200), content)