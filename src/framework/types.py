import dataclasses
from typing import NamedTuple


class ResponseT(NamedTuple):
    status: str
    headers: dict
    result: bytes


# @dataclasses.dataclass()
# class RequesT():
