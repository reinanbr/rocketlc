import pytest
import rocketlc.space_schedulle_launch as ssl


def test_sll():
    rcs = ssl.launchs()

    i = 0
    for rc in rcs:
        print(f'[{i}]',rc,'\n')
        i = i + 1