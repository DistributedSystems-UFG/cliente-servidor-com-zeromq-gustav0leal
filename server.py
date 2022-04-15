import zmq
import time
from const import * #-
context = zmq.Context()

p1 = "tcp://*:"+ PORT # how and where to connect
p2 = "tcp://*:"+ PORT2 # how and where to connect
s  = context.socket(zmq.REP)    # create reply socket
s.bind(p1)                      # bind socket to address
s.bind(p2)                      # bind socket to address

while True:
	msg = s.recv()				# wait for incoming message
	decoded_msg = bytes.decode(msg)		# decode received message
	time.sleep(1)
	if decoded_msg != 'STOP':
		# print(decoded_msg)
		mytype,a,b = decoded_msg.split(' ')
		a = float(a)
		b = float(b)
		mytype = str(mytype)
		sent_msg = 'erro'
		if mytype == 'add' :
			sent_msg = str(a+b)

		if mytype == 'subtract':
			sent_msg = str(a-b)

		if mytype == 'multiply':
			sent_msg = str(a*b)

		if mytype == 'divide':
			sent_msg = str(a/b)	

		s.send(str.encode(sent_msg))	# encode and send message
	else:
		break
