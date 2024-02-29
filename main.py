import requests

def consume_internet():
    url = 'https://jsonplaceholder.typicode.com/posts'  # You can change this to any URL you'd like to request from

    try:
        while True:
            response = requests.get(url)
            if response.status_code == 200:
                print("Received response from", url)
                print("Response text:", response.text[:100])  # Print a portion of the response text
            else:
                print("Failed to receive response from", url)

    except KeyboardInterrupt:
        print("Internet consumption stopped.")

if __name__ == "__main__":
    consume_internet()
