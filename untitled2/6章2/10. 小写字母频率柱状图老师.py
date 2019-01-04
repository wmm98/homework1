
lines = ''
while True:
    try:
        line = input()
        lines += line
    except EOFError:
        break

lower_cnt_dict = {}
for i in range(26):
    ch = chr(ord('a') + i)
    lower_cnt_dict[ch] = 0

for ch in lines:
    if ch.isalpha() and ch.islower():
        lower_cnt_dict[ch] += 1

max_cnt = 0
for cnt in lower_cnt_dict.values():
    if max_cnt < cnt:
        max_cnt = cnt

diagram = []
for i in range(max_cnt):
    diagram.append([' '] * 26)

for c in range(26):
    ch = chr(ord('a') + c)
    cnt = lower_cnt_dict[ch]
    for r in range(cnt):
        diagram[max_cnt - r - 1][c] = '*'

for r in range(max_cnt):
    print(''.join(diagram[r]))
for c in range(26):
    ch = chr(ord('a') + c)
    print(ch, end='')
