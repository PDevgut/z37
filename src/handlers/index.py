from framework.types import ResponseT
from framework.utils import read_static


def handle_index(_environ) -> ResponseT:
    base_html = read_static("_base.html").decode()
    body_html = read_static("index.html").decode()
    result = base_html.format(body=body_html)
    result = result.encode()
    status = "200 OK"
    headers = {"Content-type": "text/html"}
    return ResponseT(result=result, status=status, headers=headers)
