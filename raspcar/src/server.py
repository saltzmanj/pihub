from http.server import BaseHTTPRequestHandler, HTTPServer
import json

def pi_add(x, y):
    return x + y

class PiServerRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)

        self.send_header('Content-type','text/json')
        self.end_headers()


        cl_list = self.headers.get_all('content-length')
        content_len = int(cl_list[0])
        
        post_body = self.rfile.read(content_len)
        print(str(post_body, 'utf-8'))
        pb_json = json.loads(str(post_body, "utf-8"))
        pb_json = json.loads(pb_json)

        methodname = pb_json["method"]
        params = pb_json["params"]

        result = "None"
        result_type = "None"


        if methodname == None:
            result = "None"
            result_type = "None"
        
        elif methodname == 'pi_add':

            result = pi_add(params[0], params[1])
            result_type = "int"

        message_dict = {
            "return" : result,
            "type"   : result_type
        }

        jstring = json.dumps(message_dict)
        self.wfile.write(bytes(jstring, "utf8"))
        return

class PiServer:

    def __init__(self, address = "0.0.0.0", port=2259):
        self.address = address
        self.port = port

    def RunServer(self):
        print("Starting PiServer...")
        server_addr = (self.address, self.port)
        httpd = HTTPServer(server_addr, PiServerRequestHandler)
        print("Running server at {}:{}".format(self.address, self.port))
        httpd.serve_forever()
