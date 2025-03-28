from typing import Callable, Optional

from henago.http.request import HTTPRequest
from henago.http.response import HTTPResponse
from henago.http.static import static
from urls import url_patterns

class URLResolver:
  def resolve(self, request: HTTPRequest) -> Optional[Callable[[HTTPRequest], HTTPResponse]]:
    for url_pattern in url_patterns:
      match = url_pattern.match(request.path)
      if match:
        request.params.update(match.groupdict())
        return url_pattern.view

    return static
