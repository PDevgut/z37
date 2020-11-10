from urllib.parse import parse_qs

from framework.types import ResponseT, RequestT
from handlers.bg import handle_bg
from handlers.error500 import make_error
from handlers.handler500 import handle_500
from handlers.hello import handle_hello
from handlers.index import handle_index
from handlers.not_found import handle_404
from handlers.styles import handle_styles

handle = {"/yyy": handle_styles, "/bg.jpg/": handle_bg, "/": handle_index, "/e": make_error, "/hello": handle_hello}


def application(environ, start_response):
    try:
        url = environ["PATH_INFO"]
        RequestT.query = parse_qs(environ.get("QUERY_STRING") or ""),
        handle_name = handle.get(url, handle_404)
        ResponseT.status, ResponseT.headers, ResponseT.payload = handle_name(environ)
    except Exception:
        handle_name = handle_500
        ResponseT.status, ResponseT.headers, ResponseT.payload = handle_name(environ)

    start_response(ResponseT.status, list(ResponseT.headers.items()))
    yield ResponseT.payload
