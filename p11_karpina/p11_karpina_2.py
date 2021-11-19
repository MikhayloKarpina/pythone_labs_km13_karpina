def rrange(*args):
    return list(range(*args))

x = rrange(1, 10)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)

assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')