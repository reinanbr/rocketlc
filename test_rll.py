import pytest
from rocketlc import past_launchs as pl, future_launchs as fl



def test_rll():
    print("past launch's")
    pls = pl()

    i=0
    for l in pls['rockets']:
        print(f'[{i}]',l,'\n')
        i=i+1



    print("future launch's")
    fls = fl()

    i=0
    for l in fls['rockets']:
        print(f'[{i}]',l,'\n')
        i=i+1
