def next_index(cur_index, distance, n_len):
    return (cur_index + distance) % n_len

n = int(input())
n_str = str(n)
n_len = len(n_str)
visited_cnt = [0] * len(n_str)
cur_index = 0
visited_cnt[0] = 1
print(visited_cnt)
# [1, 0, 0, 0, 0]
while True:
    if 2 in visited_cnt:
        print("No")
        break

    cur_index = next_index(cur_index, int(n_str[cur_index]), n_len)
    if cur_index == 0 and 0 not in visited_cnt:
        print("Yes")
        break

    visited_cnt[cur_index] += 1
