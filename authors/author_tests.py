import unittest
import json

from app.modules.author.controller import AuthorController


def test_index():
    author_controller = AuthorController()
    result = author_controller.index()
    assert result == {'message': 'Hello, World!'}
