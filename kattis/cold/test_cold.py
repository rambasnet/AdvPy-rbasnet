"""Test module for main module.
"""

import unittest
from cold import answer, answer1


class TestCold(unittest.TestCase):
    """Test Cold Class.

        Must derive from unittest.TestCase class.
    """

    def setUp(self) -> None:
        self.temps1 = [-1, 100, 10000, 100000, -1000000, -99]

    def test_answer1(self) -> None:
        """_summary_
        """
        actual_ans = answer('1 -10 40 56')
        expected_ans = 1
        self.assertEqual(actual_ans, expected_ans,
                         f'{actual_ans=} != {expected_ans=}')

    def test_answer2(self) -> None:
        """_summary_
        """
        self.assertEqual(answer('-10000000'), 1)

    def test_answer3(self) -> None:
        """_summary_
        """
        self.assertEqual(answer('1000000'), 0)

    def test_answer11(self) -> None:
        """_summary_
        """
        ans = answer1(self.temps1)
        expect = 3
        self.assertEqual(ans, expect)

    def test_answer12(self) -> None:
        """_summary_
        """
        self.assertEqual(answer1([-1, -4, -99, -10]), 4)
