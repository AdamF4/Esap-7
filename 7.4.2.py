from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import subprocess


class S(BaseHTTPRequestHandler):
    def set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/jpeg')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        self.set_headers()
        subprocess.call("raspistill -n -t 250 -o 7.4.2.jpg", shell=True)
        content = open("7.4.2.jpg")
        self.wfile.write(content.read())
        content.close()


def run(server_class=HTTPServer, handler_class=S, port=8002):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":

    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

