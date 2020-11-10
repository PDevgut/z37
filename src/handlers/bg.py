from framework.utils import read_static


def handle_bg(environ):
    result = read_static("bg.jpg")
    status = "200 OK"
    headers = {"Content-type": "image/jpeg"}
    return status, headers, result
