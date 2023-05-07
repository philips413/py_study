"""
호스트 네임을 알아보자!!!
"""
import socket

in_addr = socket.gethostbyname(socket.gethostname())

print(in_addr)