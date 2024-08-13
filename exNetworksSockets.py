"""
Getting the header information of a website

Last-Modified: 
ETag: 
Content-Length: 
Cache-Control: 
Content-Type: 
"""

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True :
    data = mysock.recv(512)
    if len(data) < 1 :
        break
    print(data.decode())
mysock.close()

# Output:
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "1d3-54f6609240717"
# Content-Length: 467
# Content-Type: text/plain
