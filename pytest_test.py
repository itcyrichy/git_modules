import pytest
# some tests
from test import get_dels,simple_del_max,simplicity_check
from pro import kanon
from divisor_master import some_func

def test_f1():
    assert get_dels(10) == [1,2,5,10]
@pytest.mark.skip
def test_f2():
    assert simple_del_max([1,2,3,4,5]) == ([1,2,3,5],5)
def test_f3():
    assert simplicity_check(10) == False

def test_f4():
    assert kanon(3) == 1

@pytest.mark.xfail
def test_f5():
    assert some_func(a=5) == [1,2,3]

# Тесты запустил по-разному специально, т.к. используется input(), нужно в терминале "pytest -s" писать