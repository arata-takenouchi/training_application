import textwrap
import urllib.parse
from datetime import datetime
from pprint import pformat
from typing import Optional, Tuple

def now() -> Tuple[bytes, Optional[str], str]:
  html = f"""\
    <html>
      <body>
        <h1>Now: {datetime.now()}</h1>
      </body>
    </html>
  """
  response_body = textwrap.dedent(html).encode()

  content_type = "text/html; charset=UTF-8"

  response_line = "HTTP/1.1 200 OK\r\n"

  return response_body, content_type, response_line

def show_request(
  method: str,
  path: str,
  http_version: str,
  request_header: dict,
  request_body: bytes,
) -> Tuple[bytes, Optional[str], str]:
  html = f"""\
    <html>
    <body>
      <h1>Request Line:</h1>
      <p>
        {method} {path} {http_version}
      </p>
      <h1>Headers:</h1>
      <pre>{pformat(request_header)}</pre>
      <h1>Body:</h1>
      <pre>{request_body.decode("utf-8", "ignore")}</pre>
    </body>
    </html>
  """
  response_body = textwrap.dedent(html).encode()

  content_type = "text/html; charset=UTF-8"

  response_line = "HTTP/1.1 200 OK\r\n"

  return response_body, content_type, response_line

def parameters(
  method: str,
  request_body: bytes
) -> Tuple[bytes, Optional[str], str]:
  if method == "GET":
    response_body = b"<html><body><h1>405 Method Not Allowed</h1></body></html>"
    content_type = "text/html; charset=UTF-8"
    response_line = "HTTP/1.1 405 Method Not Allowed\r\n"

  elif method == "POST":
    post_params = urllib.parse.parse_qs(request_body.decode())
    html = f"""\
        <html>
        <body>
            <h1>Parameters:</h1>
            <pre>{pformat(post_params)}</pre>
        </body>
        </html>
    """
    response_body = textwrap.dedent(html).encode()

    content_type = "text/html; charset=UTF-8"

    response_line = "HTTP/1.1 200 OK\r\n"

  return response_body, content_type, response_line
