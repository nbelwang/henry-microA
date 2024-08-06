import zmq

def meters_to_miles(meters):
    return meters * 0.000621371

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5555")

    while True:
        meters = socket.recv_string()
        print(f"Received: {meters} meters")  # Print the received distance
        miles = meters_to_miles(float(meters))
        rounded_miles = round(miles, 2)
        socket.send_string(str(rounded_miles))

if __name__ == "__main__":
    main()