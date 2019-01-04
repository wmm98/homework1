dict_num_chr = {
}
for i in range(10):
    dict_num_chr[i] = str(i)
for i in range(10, 38):
    dict_num_chr[i] = chr(i + ord('a'))


def decimal2M(k, M):
    k_M = ''
    while k > 0:
        tail_bit = k % M
        k = k // M
        k_M = dict_num_chr[tail_bit] + k_M
    return k_M

n, b = input().split()
n = int(n)
b = int(b)
if n < 0:
    result = '-'
    n = -n
else:
    result = ''
result += decimal2M(n, b)
print(result)