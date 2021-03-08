def fatorial(n):
    fat = 1
    i = 1
    if n < 0:
         return 0
    while i <=n:
        fat= fat*1
        i = i +1
    return fat



def test_fat():
    assert fatorial(0) == 1

def test_fat1():
    assert fatorial(1) == 1

def test_fat4():
    assert fatorial(4) == 24

def test_fatex1():
    assert fatorial(5) == 120

def test_fatex2():
    assert fatorial(-10) == 0
