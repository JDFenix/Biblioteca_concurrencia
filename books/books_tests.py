import unittest
import json

from app.modules.books.controller import BooksController


def test_index():
    books_controller = BooksController()
    result = books_controller.index()
    assert result == {'message': 'Hello, World!'}
