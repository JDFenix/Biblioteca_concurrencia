import unittest
import json

from app.modules.returns.controller import ReturnsController


def test_index():
    returns_controller = ReturnsController()
    result = returns_controller.index()
    assert result == {'message': 'Hello, World!'}
