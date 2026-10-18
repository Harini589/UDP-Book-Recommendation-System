
import socket
import uuid

HOST = "127.0.0.1"
PORT = 5010

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(5)

print("=== UDP Book Recommendation Client ===")
print("Examples: genre:fantasy, author:Jane Austen")
print("Type 'exit' to quit.")

while True:
    message = input("\nEnter your search: ").strip()

    if message.lower() == "exit":
        print("Client closed.")
        break

    if not message:
        print("Please enter a search request.")
        continue

    request_id = str(uuid.uuid4())[:8]
    request = f"{request_id}|{message}"

    try:
        client.sendto(request.encode("utf-8"), (HOST, PORT))
        data, server_address = client.recvfrom(4096)
        print(f"\nRequest ID: {request_id}")
        print(data.decode("utf-8"))

    except socket.timeout:
        print(f"No response for request {request_id}. Check the server.")

client.close()
