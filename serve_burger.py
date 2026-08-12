import http.server, socketserver, os
os.chdir('/root/web-animadas/burger')
h = http.server.SimpleHTTPRequestHandler
with socketserver.ThreadingTCPServer(('0.0.0.0', 8902), h) as s:
    s.serve_forever()
