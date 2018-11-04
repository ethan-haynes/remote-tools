import sys, subprocess, os
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
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

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
