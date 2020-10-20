from framework.consts import DIR_STATIC


def application(environ, start_response):
    url = environ['PATH_INFO']
    if url == "/yyy":
        status = "200 OK"
        headers = {
            "Content-type": "text/css"
        }
        payload = read_from_styles_css()
        start_response(status, list(headers.items()))
        yield payload
    else:
        status = "200 OK"
        headers = {
            "Content-type": "text/html",
        }
        payload = read_from_index_html()

        start_response(status, list(headers.items()))

        yield payload

def read_from_index_html():
    path = DIR_STATIC / "index.html"  # Путь
    with path.open("r") as fp:  # r - режим чтения, Открыть файл
        payload = fp.read()  # Чтение и запись
    fp.close()
    payload = payload.encode()
    return payload

def read_from_styles_css():
    path = DIR_STATIC / "styles.css"  # Путь
    with path.open("r") as fp:  # r - режим чтения, Открыть файл
        payload = fp.read()  # Чтение и запись
    fp.close()
    payload = payload.encode()
    return payload

def read_from_bg_img():
    path = DIR_STATIC / "bg.jpg"  # Путь
    with path.open("r") as fp:  # r - режим чтения, Открыть файл
        payload = fp.read()  # Чтение и запись
    fp.close()
    payload = payload.encode()
    return payload