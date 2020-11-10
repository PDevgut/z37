from framework.types import ResponseT, RequestT
from framework.utils import read_static


def handle_hello(request: RequestT = None) -> ResponseT:
    name = RequestT.query
    base_html = read_static("_base.html").decode()
    hello_html = read_static("hello.html").decode()
    result = hello_html.format(name_header=name or "anon", name_value=name or "",)
    result = base_html.format(body=result)
    result = result.encode()
    status = "200 OK"
    headers = {"Content-type": "text/html"}
    return ResponseT(result=result, status=status, headers=headers)
