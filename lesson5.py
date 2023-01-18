import numpy as np
import numba as nb
import psutil
import threading
import time



def integration_decorator(*args, dx=1E-3, **kwargs):
    def decor_wrapper(func, dx2=dx):
        def res(x1, x2, dx3=dx2):
            dx228 = dx3
            c = x1
            result = 0
            for i in nb.prange((x2 - x1) / dx3):
                result += func(x1 + i * dx3)
            return result / (1 / dx3)

        return res

    return decor_wrapper


@nb.njit(fastmath=True, cache=True)
def f(x):
    return x ** 4


def deriv_decorator(dx=1E-11):
    def deriv_decor_wrapper(func, dx3=dx):
        def res(x, f=func, dx2=dx3):
            return (f(x + dx2) - f(x - dx2)) / 2 / dx2

        return res

    return deriv_decor_wrapper


def deriv(f, x, dx=1E-11):
    return (f(x + dx) - f(x - dx)) / 2 / dx


@deriv_decorator(dx=1E-11)
def f2(x):
    return f(x)


@integration_decorator(dx=1E-7)
def f3(x):
    return f(x)


@nb.njit(fastmath=True, parallel=True, cache=True)
def gg(x1, x2, dx3=1E-6):
    result = 0.000001
    for i in nb.prange(int((x2 - x1) / dx3)):
        result += f(x1 + i * dx3)
    return result / (1 / dx3)

def show_usage():
    while not gg2:
        print(f"\r{psutil.cpu_percent()}", end='')
        time.sleep(0.5)

xx1, xx2 = map(float, input().split())
gg2=False
t = threading.Thread(target=show_usage)
t.start()
x = gg(xx1, xx2)
gg2=True
t.join()
print()
print(x)