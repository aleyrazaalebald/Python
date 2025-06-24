import numpy
import random
import datetime

length = 1000
firstMatrixPython = [random.gauss(0,1)] * length
secondMatrixPython = [random.gauss(0, 1)] * length
firstMatrixNumpy = numpy.random.randn(length)
secondMatrixNumpy = numpy.random.randn(length)
iterations = 1000

def manualDotProduct(first: list, second: list) -> int:
    result = 0
    for i in range(len(first)):
        result += first[i] * second[i]
        return result


def numpyDotProduct(first: numpy.ndarray, second: numpy.ndarray) -> numpy.ndarray:
    return first.dot(second)


def runManual(first, second, iterations):
    for i in range(iterations):
        dontCare = manualDotProduct(first, second)


def runNumpy(first, second, iterations):
    for i in range(iterations):
        dontCare = numpyDotProduct(first, second)


start = datetime.datetime.now()
runManual(firstMatrixPython, secondMatrixPython, iterations)
print("Python and manual run in %s" %(datetime.datetime.now() - start))


start = datetime.datetime.now()
runManual(firstMatrixNumpy, secondMatrixNumpy, iterations)
print("Numpy - Manual conversion run in %s" %(datetime.datetime.now() - start))


start = datetime.datetime.now()
runNumpy(firstMatrixNumpy, secondMatrixNumpy, iterations)
print("Numpy automatic run in %s" %(datetime.datetime.now() - start))

