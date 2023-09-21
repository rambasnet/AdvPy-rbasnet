import main
import unittest

class TestHello(unittest.TestCase):
  def setUp(self):
    self.data = [1, 2]
    print('setup called...')

  def tearDown(self) -> None:
    print('tear down called...')
    self.data = None
    return super().tearDown()

  def test_answer(self):
    ans = main.answer()
    expected = 'Hello World!'
    print('me')
    self.assertEqual(ans, expected, "din't match...")


