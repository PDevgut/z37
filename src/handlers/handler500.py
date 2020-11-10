import traceback

from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import read_static


def handle_500(_request: RequestT = None) -> ResponseT:
    base_html = read_static("_base.html").decode()
    error_html = str(traceback.format_exc())
    result = base_html.format(body=error_html)
    result = result.encode()

    status = "500 Internal Server Error"
    headers = {"Content-type": "text/html"}

    return ResponseT(result=result, status=status, headers=headers)