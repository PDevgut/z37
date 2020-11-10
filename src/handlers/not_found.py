from framework.utils import read_static


def handle_404(environ):
    base_html = read_static("_base.html").decode()
    body_html = read_static("404.html").decode()
    result = base_html.format(body=body_html)
    result = result.encode()
    status = "200 OK"
    headers = {"Content-type": "text/html"}
    return status, headers, result
