from spin_http import Response
from random import randrange, uniform

def handle_request(request):
    # randrange gives you an integral value
    return Response(200,
                    {"content-type": "text/plain"},
                    bytes(f"Hello iadsuhfpaoidsuhfpasoiduhfpüoaihsdü", "utf-8"))
