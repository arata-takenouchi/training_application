from typing import Optional, Union

class HTTPResponse:
  status_code: int
  content_type: Optional[str]
  body: Union[bytes, str]
  headers: dict

  def __init__(
    self,
    status_code: int = 200,
    headers: dict = None,
    content_type: str = None,
    body: Union[bytes, str] = b"",
  ):
    if headers is None:
      headers = {}

    self.status_code = status_code
    self.headers = headers
    self.content_type = content_type
    self.body = body