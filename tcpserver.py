import socket

class TCPServer:
  """
  TCPサーバーのクラス
  """
  def serve(self):
    """
    サーバー起動
    """

    print("=== start server ===")

    try:
      server_socket = socket.socket()
      server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

      server_socket.bind(("localhost", 8080))
      server_socket.listen(10)

      print("=== wait client connection ===")
      (client_socket, address) = server_socket.accept()
      print(f"=== complete client connection remote_address: {address} ===")

      request = client_socket.recv(4096)

      with open("server_recv.txt", "wb") as f:
        f.write(request)

      client_socket.close()

    finally:
      print("=== stop server ===")

if __name__ == '__main__':
  server = TCPServer()
  server.serve()
