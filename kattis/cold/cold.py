"""
Katti cold solution.

"""

import sys
from typing import List

__author__ = "Ram Basnet"
__date__ = "Sep 19, 2023"


def answer(data: str) -> int:
    """Finda and returns -ve temps in data

    Args:
        data (str): list of temps separated by space

    Returns:
        int: count of -ve temps
    """
    return data.count('-')


def answer1(temps: List[int]) -> int:
    """_summary_

    Args:
        temps (List[int]): _description_

    Returns:
        int: _description_
    """
    count = 0
    for t in temps:
        if t < 0:
            count += 1
    return count


def main() -> None:
    """Main function.
    """

    temp_count = input()
    temps = input()
    print(f'{temp_count=} {temps=}', file=sys.stderr)
    print(answer(temps))


if __name__ == "__main__":
    main()
