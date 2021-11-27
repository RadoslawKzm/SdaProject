"""We use sets for high performance membership testing"""
import time

st1 = set(range(10_000_000))

st2 = {-2, -1, 0, 1, 2, 3, 10}
st3 = {10, 11}
st4 = {10, 100, 101}
st5 = {10, 1000, 1001}

union = st1.union(st2)
intersection = st1.intersection(st2)
inter2 = st1 & st2 & st3 & st4 & st5

diff = st2 - st3
