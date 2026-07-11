import http.server
import json

PORT = 6666
ultimo_mensaje = ""
ultimo_shell = ""


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/messages':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(ultimo_mensaje.encode())
        elif self.path == '/shell_messages':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(ultimo_shell.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        global ultimo_mensaje, ultimo_shell
        
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length).decode()
        
        # Intentar parsear como JSON
        try:
            data = json.loads(body)
            mensaje = data.get('msg', body)
        except:
            mensaje = body
        
        if self.path == '/send':
            ultimo_mensaje = mensaje
        elif self.path == '/shell':
            ultimo_shell = mensaje
        else:
            self.send_response(404)
            self.end_headers()
            return
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

    def log_message(self, format, *args):
        pass


print(f"Servidor en http://localhost:{PORT}")
print("GET  /messages        - Ver último mensaje")
print("GET  /shell_messages  - Ver último mensaje de shell")
print("POST /send            - Guardar mensaje")
print("POST /shell           - Guardar mensaje de shell")
http.server.HTTPServer(('', PORT), Handler).serve_forever()
