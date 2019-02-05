#import responder.status_codes as status_codes
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("[{\"msg\": \"Hello World!\"}]")




#import entity

#def respond(func):
#    """HTTPリクエストハンドラの共通的なデコレータ"""

#    def wrapper(*args, **kwargs):
        # 第3引数が、responderのResponseオブジェクト
#        resp = args[2]

        # ドメインのエラーを、HTTPのステータスコードに対応づける
#        try:
#            result = func(*args, **kwargs)
#        except entity.NotFound:
            #resp.status_code = status_codes.HTTP_404
#            resp.status_code = HttpResponse(status=404)
#        else:
#            if isinstance(result, tuple):
#                resp.status_code = result[0]
#                resp.media = result[1]
#            else:
#                resp.status_code = result

#    return wrapper
