__author__ = 'Administrator'

import socket
import re

COMMAND_PREFIX = "command"
HEARTBEAT = "hbSync"

HOST,PORT = host,port

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    while(1):
        sock.connect((HOST,PORT))
        sock.sendall("I am connected !")
        data = ""
        while(1):
            data_buf = sock.recv(1024)
            if HEARTBEAT in data_buf:
                send_response()
                continue
            data = "".join([data,data_buf])
            matchobj = re.match(r'^command: (.*) End',data_buf,re.I)
            if matchobj is not None:
                cmd = matchobj.group(1)
                process_command(cmd)
            else:
                continue
except:
    print "Error"
finally:
    sock.close()




