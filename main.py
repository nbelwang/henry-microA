import sender

def main():
    meters = 450  # example distance in meters
    miles = sender.send_distance(meters)

    # test code to print to console
    print(f"{meters} meters is equal to {miles} miles")

if __name__ == "__main__":
    main()