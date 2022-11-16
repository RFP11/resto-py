
def __init__(self):
    self._jml = []
    self._total = int(0)


def jml(self, a):
    self._jml.append(int(a))


def jml(self):
    return self._jml


def total(self, a):
    self._total = a


def total(self):
    arraysum(self._jml)
    return self._total


def arraysum(arr):
    sum = 0
    for element in arr:
        sum += element
    return sum
