import pytest
from hypothesis import given, strategies as st

import my_package.adding as my_add

@given(st.integers())
def test_adds_one(num):
    print(f"Trying num={num}, x=1...")
    x = 1
    result = my_add.adds_x(num, x)
    expect = num + x
    assert result == expect, f"adds_x should return {expect} when given {num} and {x}, but instead returned {result}"
    
@given(st.integers())
def test_adds_one_fail_on_zero(num):
    print(f"Trying num={num}, x=1...")
    x = 1
    result = my_add.adds_x(num, x)
    if num == 0:
        result = 0
    expect = num + x
    assert result == expect, f"adds_x should return {expect} when given {num} and {x}, but instead returned {result}"