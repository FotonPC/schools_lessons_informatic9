import numpy as np


def gg(symbol):
    return char_to_int[symbol]


a = list('0123456789')
char_to_int = dict()
for (i, ch) in enumerate(a):
    char_to_int[ch] = i

raw_first = '0' + input()
raw_second = '0' + input()

max_len = max(len(raw_first), len(raw_second))
raw_first = raw_first.zfill(max_len)
raw_second = raw_second.zfill(max_len)

first_num = np.array(list(map(gg, list(raw_first))))
second_num = np.array(list(map(gg, list(raw_second))))

res_raw = first_num + second_num

i = len(res_raw) - 1

while i > 0:
    res_raw[i - 1] += res_raw[i] // 10
    res_raw[i] = res_raw[i] % 10
    i -= 1
res = list(res_raw)
if res[0] == 0:
    res = res[1::]
print(''.join(list(map(str, res))))
