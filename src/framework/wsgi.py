from framework.types import ResponseT
from handlers.bg import handle_bg
from handlers.index import handle_index
from handlers.not_found import handle_404
from handlers.styles import handle_styles

handle = {"/yyy": handle_styles, "/bg.jpg/": handle_bg, "/": handle_index}


def application(environ, start_response):

    url = environ["PATH_INFO"]
    handle_name = handle.get(url, handle_404)
    ResponseT.status, ResponseT.headers, ResponseT.payload = handle_name(environ)
    start_response(ResponseT.status, list(ResponseT.headers.items()))
    yield ResponseT.payload
