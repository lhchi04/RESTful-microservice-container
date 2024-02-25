from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

# Sample data (dictionary of books)
books = {}

# Function to generate a unique ID for each book
def generate_book_id():
    return str(len(books) + 1)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    book_id = generate_book_id()
    books[book_id] = new_book
    return jsonify({'id': book_id, 'book': new_book})

@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    if book_id in books:
        return jsonify(books[book_id])
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    if book_id in books:
        updated_book = request.json
        books[book_id] = updated_book
        return jsonify({'id': book_id, 'book': updated_book})
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id in books:
        del books[book_id]
        return jsonify({'message': 'Book deleted'})
    else:
        return jsonify({'error': 'Book not found'}), 404

# Swagger UI configuration
SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Library Management API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
