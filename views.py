import textwrap
import urllib.parse
from datetime import datetime
from pprint import pformat

from henago.http.request import HTTPRequest
from henago.http.response import HTTPResponse
from henago.template.render import render

def now(request: HTTPRequest) -> HTTPResponse:
  context = {"now": datetime.now()}
  html = render("now.html", context)

  body = html.encode()
  content_type = "text/html; charset=UTF-8"

  return HTTPResponse(body=body, content_type=content_type, status_code=200)

def show_request(request: HTTPRequest) -> HTTPResponse:
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

  return HTTPResponse(body=response_body, content_type=content_type, status_code=200)

def parameters(request: HTTPRequest) -> HTTPResponse:
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

  return HTTPResponse(body=response_body, content_type=content_type, status_code=200)

def user_profile(request: HTTPRequest) -> HTTPResponse:
  user_id = request.params["user_id"]
  html = f"""\
      <html>
      <body>
          <h1>プロフール</h1>
          <pre>ID: {user_id}</pre>
      </body>
      </html>
  """
  body = textwrap.dedent(html).encode()
  content_type = "text/html; charset=UTF-8"
  status_code = 200

  return HTTPResponse(body=body, content_type=content_type, status_code=status_code)
