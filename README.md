# RESTful-microservice-container
# Simple Library Management API

This is a simple RESTful microservice built using Flask, which allows you to manage a collection of books in a library. It provides endpoints to perform CRUD operations on books and is accompanied by Swagger UI for easy interaction.

## Requirements

- Docker

## Getting Started

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/library-management-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd library-management-api
    ```

3. Build the Docker image:

    ```bash
    docker build -t library-management-api .
    ```

4. Run the Docker container:

    ```bash
    docker run -d -p 2369:2369 library-management-api
    ```

    The application should now be running and accessible at http://localhost:2369.

## API Endpoints

### Get all books

- **URL:** `/books`
- **Method:** `GET`
- **Description:** Retrieves a list of all books in the library.
- **Response:** JSON object containing an array of books.

### Add a new book

- **URL:** `/books`
- **Method:** `POST`
- **Description:** Adds a new book to the library.
- **Request Body:** JSON object with `title` and `author` fields.
- **Response:** JSON object containing the index of the newly added book and its details.

### Get details of a specific book

- **URL:** `/books/<index>`
- **Method:** `GET`
- **Description:** Retrieves details of a specific book by its index.
- **Parameters:** `index` - Index of the book to retrieve.
- **Response:** JSON object containing details of the requested book.

### Update details of a specific book

- **URL:** `/books/<index>`
- **Method:** `PUT`
- **Description:** Updates details of a specific book by its index.
- **Parameters:** `index` - Index of the book to update.
- **Request Body:** JSON object with updated `title` and/or `author`.
- **Response:** JSON object containing details of the updated book.

### Delete a specific book

- **URL:** `/books/<index>`
- **Method:** `DELETE`
- **Description:** Deletes a specific book by its index.
- **Parameters:** `index` - Index of the book to delete.
- **Response:** JSON object confirming the deletion of the book.

### Swagger UI

You can also interact with the API using Swagger UI. Visit http://localhost:2369/swagger to explore the API documentation interactively.


