from handlers.bg import handle_bg
from handlers.not_found import handle_404
from handlers.styles import handle_styles
from hendlers.index import handle_index

handle = {"/yyy": handle_styles, "/bg.jpg/": handle_bg, "/": handle_index}

def application(environ, start_response):

    url = environ["PATH_INFO"]
    handle_name = handle.get(url, handle_404)
    status, headers, payload = handle_name(environ)
    start_response(status, list(headers.items()))
    yield payload


