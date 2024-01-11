#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
class TestBase(unittest.TestCase):
    """Test class for Base class."""
    def test_to_json_string(self):
        data = [{"key": "value"}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"key": "value"}]')

    def test_from_json_string(self):
        json_string = '[{"key": "value"}]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [{"key": "value"}])

    def test_create(self):
        dictionary = {"id": 1, "key": "value"}
        result = Base.create(**dictionary)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.key, "value")



if __name__ == '__main__':
    unittest.main()

