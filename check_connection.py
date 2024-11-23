# This Python file uses the following encoding: utf-8
import socket

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("cdnjs.cloudflare.com", 443))
        return True
    except OSError:
        pass
    return False
