
import socket
import json
import os
import logging

# Server configuration
HOST = "127.0.0.1"
PORT = 5010

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOKS_FILE = os.path.join(BASE_DIR, "books.json")
LOG_FILE = os.path.join(BASE_DIR, "server.log")

# Configure server logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Load the book catalogue
with open(BOOKS_FILE, "r", encoding="utf-8") as file:
    books = json.load(file)

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("UDP Book Recommendation Server is running!")
print(f"Listening on {HOST}:{PORT}")
print(f"Loaded {len(books)} books.")
print(f"Logging to {LOG_FILE}")
print("Waiting for client requests...")

while True:
    try:
        # Receive a request from a client
        data, client_address = server.recvfrom(4096)
        message = data.decode("utf-8").strip()

        # Extract request ID and query
        if "|" in message:
            request_id, query = message.split("|", 1)
        else:
            request_id = "UNKNOWN"
            query = message

        logging.info(
            "Request ID=%s | Client=%s | Query=%s",
            request_id, client_address, query
        )

        print(f"\nRequest ID: {request_id}")
        print(f"Request from {client_address}: {query}")

        # Validate the request
        parts = query.split(":", 1)

        if len(parts) != 2:
            response = (
                "Invalid request. Use genre:fantasy, "
                "author:Jane Austen, or recommend:fantasy"
            )
        else:
            search_type = parts[0].strip().lower()
            search_value = parts[1].strip().lower()

            if search_type not in ("genre", "author", "recommend"):
                response = (
                    "Invalid search type. "
                    "Use genre, author, or recommend."
                )

            elif not search_value:
                response = "Please provide a genre or author name."

            else:
                matches = []

                # Search the catalogue
                for book in books:
                    if search_type in ("genre", "recommend"):
                        if search_value in book["genre"].lower():
                            matches.append(book)

                    elif search_type == "author":
                        if search_value in book["author"].lower():
                            matches.append(book)

                # Build the response
                if matches:
                    if search_type == "recommend":
                        response_lines = [
                            f"Book recommendations for '{search_value}':"
                        ]
                    else:
                        response_lines = ["Matching books:"]

                    for book in matches:
                        response_lines.append(
                            f'{book["title"]} by {book["author"]} '
                            f'({book["genre"]})'
                        )

                    response = "\n".join(response_lines)

                else:
                    response = (
                        "No matching books found. "
                        "Try another genre or author."
                    )

        # Send the response to the requesting client
        server.sendto(
            response.encode("utf-8"),
            client_address
        )

        logging.info(
            "Request ID=%s | Response sent | Bytes=%d",
            request_id,
            len(response.encode("utf-8"))
        )

        print(f"Response sent for request ID: {request_id}")

    except Exception as error:
        logging.exception("Error while processing a request")
        print(f"Error: {error}")
