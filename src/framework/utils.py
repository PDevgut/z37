from framework.consts import DIR_STATIC


def read_static(file_name: str) -> bytes:
    path = DIR_STATIC / file_name  # Путь
    with path.open("rb") as fp:  # r - режим чтения, Открыть файл
        payload = fp.read()  # Чтение и запись
    return payload
