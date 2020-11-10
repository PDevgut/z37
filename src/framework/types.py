import dataclasses
from typing import NamedTuple, Optional, Callable


class ResponseT(NamedTuple):
    status: str
    headers: dict
    result: bytes

@dataclasses.dataclass
class RequestT:
    method: str
    path: str
    headers: dict
    query: Optional[dict] = None

HandlerT = Callable[[RequestT], ResponseT]

class StaticT(NamedTuple):
    content: bytes
    content_type: str
