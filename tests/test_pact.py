import unittest

from .pact_player import PactPlayer
from controller import controller
#from books import controller

class TestPact(unittest.TestCase):
    def test_hello(self):

        api = controller.create_server()
        PactPlayer('hello.json').run(self, api)
