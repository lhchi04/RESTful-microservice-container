import os
import json
import logging
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

# Sample data (list of books)
books = []

# Function to search for a book by index
def get_book_by_index(index):
    try:
        return books[int(index)]
    except IndexError:
        return None

# Add /config route
@app.route('/config', methods=['GET'])
def get_config():
    config_data = {key: value for key, value in os.environ.items()}
    app.logger.info("Config data: %s", json.dumps(config_data))
    print('Environment data:', config_data)
    return jsonify(config_data)

# Add /fib route
@app.route('/fib', methods=['GET'])
def get_fibonacci():
    length = int(request.args.get('length', 10))
    fibonacci_sequence = [0, 1]
    for i in range(2, length):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    return jsonify(fibonacci_sequence)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify({'index': len(books) - 1, 'book': new_book})

@app.route('/books/<index>', methods=['GET'])
def get_book(index):
    book = get_book_by_index(index)
    if book is not None:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<index>', methods=['PUT'])
def update_book(index):
    book = get_book_by_index(index)
    if book is not None:
        updated_book = request.json
        books[int(index)] = updated_book
        return jsonify({'index': index, 'book': updated_book})
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<index>', methods=['DELETE'])
def delete_book(index):
    book = get_book_by_index(index)
    if book is not None:
        del books[int(index)]
        return jsonify({'message': 'Book deleted'})
    else:
        return jsonify({'error': 'Book not found'}), 404

# Swagger UI configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Library Management API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
