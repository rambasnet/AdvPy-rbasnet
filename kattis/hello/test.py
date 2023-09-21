import math
import sys
import unittest
from unittest.mock import patch
from io import StringIO

def hello():
  return 'hello'

math.sin = hello

def read_data():
  x = sys.stdin.readline()
  return x

class Test(unittest.TestCase):

  @patch('sys.stdin', StringIO("Data"))
  def test_read_data(self):
    a = read_data()
    print(a)
    self.assertEqual(a, 'Data1')
    #self.assertEqual(read_data(), stdin.readline())


#unittest.main()




