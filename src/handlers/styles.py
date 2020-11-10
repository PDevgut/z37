from framework.utils import read_static


def handle_styles(environ):

    result = read_static("styles.css")
    status = "200 OK"
    headers = {"Content-type": "text/css"}
    return status, headers, result
