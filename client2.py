import zmq
import random

from const import *
context = zmq.Context()

p1 = "tcp://"+ SERVER +":"+ PORT2 # how and where to connect
s  = context.socket(zmq.REQ)    # create request socket
# print("Escreva a operacao(add,subtract,multiply,divide) e dois numeros na mesma linha e separados por espaço")
l = ['add','subtract','multiply','divide']
s.connect(p1)                   # block until connected
for i in range(10):
	msg = l[random.randint(0,3)] + ' ' + str(random.random()) + ' ' + str(random.random())
	s.send(str.encode(msg))          # send message
	message = s.recv()              # block until response
	# s.send(b"STOP")                 # tell server to stop
	print(msg)
	print (bytes.decode(message))                 # print result

# s.send(b"STOP") 
