import re
from re import Match
from typing import Callable, Optional

from henago.http.request import HTTPRequest
from henago.http.response import HTTPResponse

class URLPattern:
  pattern: str
  view: Callable[[HTTPRequest], HTTPResponse]

  def __init__(self, pattern: str, view: Callable[[HTTPRequest], HTTPResponse]):
    self.pattern = pattern
    self.view = view

  def match(self, path: str) -> Optional[Match]:
    re_pattern = re.sub(r"<(.+?)>", r"(?P<\1>[^/]+)", url_pattern)
    return re.match(re_pattern, path)