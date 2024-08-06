# Distance Converter Microservice

This microservice allows you to convert distances from meters to miles using ZeroMQ for communication! 

#### This microservice contains: 
- main.py: an example file of how you would call the microservice. 
- sender.py: sends the distance (meters) to the microservice and receives the converted distance in miles.
- receiver.py: listens for incoming requests, converts the received distance from meters to miles, and sends back the result.

## Communication Contract

### Requesting Data

To request data from the microservice, you need to call the `send_distance` function defined in the `sender.py` file. This function sends a distance in meters to the microservice and receives the converted distance in miles.

#### Example Call

Here’s an example of how to use the `send_distance` function in `main.py`:

```python
import sender

def main():
    meters = 450  # example distance in meters
    miles = sender.send_distance(meters)

    # test code to print to console, use miles to fit your implementation
    print(f"{meters} meters is equal to {miles} miles")

if __name__ == "__main__":
    main()
```

### Receiving Data

To receive data from the microservice, the `receiver.py` file listens for incoming requests. When a distance is received, it processes the request and sends back the converted distance in miles.

1. Start the microservice by running `receiver.py `

`python receiver.py`

2. Call the send_distance function in main.py as shown above to send a distance and receive the converted value. Whenever you run main, the microservice will return back a value. 

## UML Sequence Diagram

![UML Sequence Diagram](diagram.png)

