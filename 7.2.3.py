from sense_hat import SenseHat
# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# import SocketServer
from http.server import BaseHTTPRequestHandler, HTTPServer


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        sense = SenseHat()
        self._set_headers()
        temperature = round(sense.get_temperature(), 4)
        humidity = round(sense.get_humidity(), 4)
        # print("Temperature: ", temperature, " Humidity: ", humidity)
        self.wfile.write(bytes("{“temperature”:"+str(temperature)+", “humidity”:"+str(humidity)+"}", "utf-8"))


def run(server_class=HTTPServer, handler_class=S, port=8001):
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
