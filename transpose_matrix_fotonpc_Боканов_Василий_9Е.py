import numpy as np
import numba as nb
import time

h = int(input("Сколько строк? :"))
w = int(input("Сколько столбцов? :"))

matrix = [list(map(float, input().split())) for i in range(h)]


@nb.njit(cache=True, fastmath=True, parallel=True)
def transpose(matrix, width, height):
    res = np.zeros((width, height))
    for i in nb.prange(width):
        for j in nb.prange(height):
            res[i][j] = matrix[j][i]
    return res


def format_num(num, l):
    l2 = len(str(num))
    return str(num) + ' ' * (l - l2)


def out_matrix(matrix, width, height):
    mx_len = len(str(np.max(matrix)))
    out = ''
    for i in range(height):
        out += "+" + ("-" * (mx_len + 1) + '-+') * width + '\n'
        out += '| '
        for j in range(width):
            out += format_num(matrix[i][j], mx_len) + ' | '
        out += '\n'
    out += "+" + ("-" * (mx_len + 1) + '-+') * width
    return out


b = time.perf_counter()
print(out_matrix(transpose(np.array(matrix), w, h), w, h))

# w = 12345
# h = 12345

# Если ставить больше то -
# numpy.core._exceptions._ArrayMemoryError:
#        Unable to allocate 114.GiB for an array
#        with shape (123456, 123456)
#        and data type float64

# transpose(np.random.sample((w, h)), w, h)
e = time.perf_counter()
print("time:", e - b)
print("Если запускаете код первый раз то досточно большое время пре-jit-компилирования")
