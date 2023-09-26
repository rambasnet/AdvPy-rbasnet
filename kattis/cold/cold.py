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

    temp_count = input().strip()
    temps = sys.stdin.readline().strip().split()
    # int_temps = [int(t) for t in temps]
    int_temps = map(int, temps)
    # for t in temps:
    #    int_temps.append(int(t))
    int_temps = [0]*int(temp_count)
    for i in range(temp_count):
        int_temps[i] = int(sys.stdin.readline())

    print(f'{temp_count=} {temps=}', file=sys.stderr)
    print(answer1(int_temps))


if __name__ == "__main__":
    main()
