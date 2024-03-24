#!/usr/bin/python3
import io
import unittest
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def test_help(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            self.assertIn("Documented commands (type help <topic>):", output)

    def test_show(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234-1234-1234")
            output = f.getvalue()
            self.assertIn("** no instance found **", output)

    def test_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue()
            self.assertIn("** class name missing **", output)

    def test_destroy(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234-1234-1234")
            output = f.getvalue()
            self.assertIn("** no instance found **", output)

    def test_update(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234-1234-1234 name=John")
            output = f.getvalue()
            self.assertIn("** no instance found **", output)

    def test_all(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            output = f.getvalue()
            self.assertIn("[]", output)

    def test_count(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            output = f.getvalue()
            self.assertIn("0", output)


if __name__ == '__main__':
    unittest.main()
