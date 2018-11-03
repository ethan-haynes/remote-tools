import sys, subprocess, os
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        data = self.request.recv(1024).strip().split(b'\n')
        
        print("{} wrote:".format(self.client_address[0]))
        
        if data:
            method, path, protocol = data.pop(0).split(b' ')
            if method == b'GET':
                if os.path.exists(path):
                    disk_usage = subprocess.run(["du", "-x", path], capture_output=True)
                    disk_usage = disk_usage.stdout.splitlines()
                    out = {}
                    for file in disk_usage:
                        f_bytes, f_name = file.split('\t'.encode())
                        out[f_name.decode("utf-8")] = int(f_bytes)
                    print(out)
                    print(method, path, protocol)
        
        self.request.sendall(str(data).encode())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

