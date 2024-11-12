import unittest
import json

from app.modules.lending.controller import LendingController


def test_index():
    lending_controller = LendingController()
    result = lending_controller.index()
    assert result == {'message': 'Hello, World!'}
