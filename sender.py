import zmq

def send_distance(meters):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:5555")

    socket.send_string(str(meters))
    miles = socket.recv_string()
    return miles