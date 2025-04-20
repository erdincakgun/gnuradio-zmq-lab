import zmq
import numpy as np
import time
import matplotlib.pyplot as plt

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'')

while True:
    if socket.poll(10) != 0:
        msg = socket.recv()
        data = np.frombuffer(msg, dtype=np.complex64, count=-1)
        plt.plot(np.real(data))
        plt.plot(np.imag(data))
        plt.show()
    else:
        time.sleep(0.1)