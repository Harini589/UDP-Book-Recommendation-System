
# UDP-Based Distributed Book Recommendation System

## Project Overview

This project implements a client-server book search and recommendation system using Python and User Datagram Protocol (UDP).

A client sends a search request to the server. The server processes the request using a JSON book catalogue and sends the matching results back to the client.

Each request can include a unique request ID, and the server records request details and response information in a log file.

## Features

- Search books by genre
- Search books by author
- Get genre-based book recommendations
- UDP-based client-server communication
- Unique request IDs for tracking requests
- Server-side logging
- Support for multiple client instances

## Technologies Used

- Python 3
- UDP sockets
- JSON
- Python logging module
- Visual Studio Code

## Project Structure

 
## System Architecture

```text
+----------------------+
|         User         |
+----------------------+
           |
           v
+----------------------+
|    UDP Client        |
|  client.py           |
+----------------------+
           |
           | UDP Request
           v
+----------------------+
|    UDP Server        |
|  server.py           |
+----------------------+
      |          |
      v          v
+-----------+ +------------+
| books.json| | server.log |
| Catalogue | |   Logging  |
+-----------+ +------------+
           |
           v
+----------------------+
|   UDP Response       |
|  Matching book data  |
+----------------------+
           |
           v
+----------------------+
| Client displays      |
| search results       |
+----------------------+
```


## How It Works

1. The client accepts a search query from the user.
2. The client generates a unique request ID.
3. The query and request ID are sent to the server using UDP.
4. The server processes the request and searches the book catalogue.
5. The server sends the matching results to the client.
6. The server records request and response information in server.log.

## Setup and Execution

### Requirements

- Python 3 installed
- All project files in the same folder

### Start the server

Open a terminal in the project folder and run:

    python server.py

The server listens on 127.0.0.1, port 5010.

Keep the server running.

### Start the client

Open a second terminal in the same project folder and run:

    python client.py

Enter one of the following queries.

### Example Queries

    genre:fantasy
    author:Jane Austen
    recommend:fantasy
    recommend:mystery

Type `exit` to close the client.

## Sample Output

    Request ID: 4436bcbf
    Book recommendations for 'fantasy':
    The Hobbit by J.R.R. Tolkien (fantasy)
    Harry Potter and the Philosopher's Stone by J.K. Rowling (fantasy)

## Logging

The server records incoming requests and response details in `server.log`. The log includes request IDs, client addresses, queries, and response sizes.

## Current Limitations

- The server uses a local IP address, so the current setup is intended for testing on one computer.
- UDP does not guarantee delivery or ordering of messages.
- The catalogue contains a small set of books stored in a JSON file.
- Recommendations are based on genre matching, not machine learning or user ratings.

## Future Enhancements

- Add a larger book catalogue
- Rank recommendations using user preferences
- Support clients on different computers
- Add automated tests and improved error handling

## Author

Harini

