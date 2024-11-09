import unittest
import json

from app.modules.users.controller import UsersController


def test_index():
    users_controller = UsersController()
    result = users_controller.index()
    assert result == {'message': 'Hello, World!'}
