import http.client
import json

# Sent json has format:
# {
#   "method": "<method name>",
#   "params": [list of parameters]
# }
#
#
class PiSocket:

    def __init__(self, ip = "0.0.0.0", port = 2259, to = 10):
        self.ip = ip
        self.port = port
        self.timeout = to

    def exec(self, methodname, paramslist):
        conn = http.client.HTTPConnection(self.ip, self.port, self.timeout)
        rpcstring = {
            "method" : methodname,
            "params" : paramslist
            }
        rpcjson = json.dumps(rpcstring)
        # print(rpcjson)
        # print(len(rpcjson))
        
        rpcjsonutf8 = bytes(json.dumps(rpcjson), "utf-8")
        headers = {"content-length": str(len(rpcjsonutf8))}


        conn.request("POST", "/", rpcjsonutf8, headers = headers)
        s = conn.getresponse().read()
        # print(str(s, "utf-8"))
        resp = json.loads(str(s, "utf-8"))
        return resp

