import mimetypes
import random

from framework.consts import DIR_STATIC


def application(environ, start_response):
    url = environ["PATH_INFO"]

    file_names = {"/yyy": "styles.css", "/bg.jpg/": "bg.jpg", "/": "index.html"}

    file_name = file_names.get(url)

    status = "200 OK"
    headers = {"Content-type": mimetypes.MimeTypes().guess_type(file_name)[0]}
    payload = read_static(file_name)
    start_response(status, list(headers.items()))
    yield payload


# def read_from_index_html():
#     path = DIR_STATIC / "index.html"  # Путь
#     with path.open("r") as fp:  # r - режим чтения, Открыть файл
#         payload = fp.read()  # Чтение и запись
#     fp.close()
#     payload = payload.encode()
#     return payload
# def read_from_styles_css():
#     path = DIR_STATIC / "styles.css"  # Путь
#     with path.open("r") as fp:  # r - режим чтения, Открыть файл
#         payload = fp.read()  # Чтение и запись
#     fp.close()
#     payload = payload.encode()
#     return payload
# def read_from_bg_img():
#     path = DIR_STATIC / "bg.jpg"  # Путь
#     with path.open("rb") as fp:  # r - режим чтения, Открыть файл
#         payload = fp.read()  # Чтение и запись
#
#     return payload


def read_static(file_name: str) -> bytes:
    path = DIR_STATIC / file_name  # Путь
    with path.open("rb") as fp:  # r - режим чтения, Открыть файл
        payload = fp.read()  # Чтение и запись
    return payload

def generate_404(environ) -> bytes:
    url = environ["PATH_INFO"]
    pin = random.randint(1,1000)
    msg = f"Hello world! Your path {url} not found. Pin {pin}"
    return msg.encode()