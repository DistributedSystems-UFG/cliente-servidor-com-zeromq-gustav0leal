import zmq
from const import *
context = zmq.Context()

p1 = "tcp://"+ SERVER +":"+ PORT # how and where to connect
s  = context.socket(zmq.REQ)    # create request socket
print("Escreva a operacao(add,subtract,multiply,divide) e dois numeros na mesma linha e separados por espaço")

msg = input()

s.connect(p1)                   # block until connected
s.send(str.encode(msg))          # send message
message = s.recv()              # block until response
s.send(b"STOP")                 # tell server to stop
print (bytes.decode(message))                 # print result
