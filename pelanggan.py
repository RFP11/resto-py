def __init__(self):
    self._uang = int(0)
    self._total = int(0)
    self._member = bool(False)


def uang(self, a):
    self._uang = a


def uang(self):
    return self._uang


def total(self, a):
    self._total = a


def total(self):
    return self._total


def member(self, x):
    self._member = bool(x)


def member(self):
    return self._member


def kembalian(x, y):
    if x >= y:
        return int(x)-int(y)
    else:
        print('Uang mu tidak cukup')
