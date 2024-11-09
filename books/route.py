from flask import Blueprint, make_response, jsonify
from .controller import BooksController


books_bp = Blueprint('books', __name__)
books_controller = BooksController()
@books_bp.route('/', methods=['GET'])
def index():
    """ Example endpoint with simple greeting.
    ---
    tags:
      - Example API
    responses:
      200:
        description: A simple greeting
        schema:
          type: object
          properties:
            data:
              type: object
              properties:
                message:
                  type: string
                  example: "Hello World!"
    """
    result=books_controller.index()
    return make_response(jsonify(data=result))
      