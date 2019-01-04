def is_prime(n):
    '''n是素数吗'''
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def add_one_number(r_list, N, prime_list):
    # print("add_one_number: r_list=", r_list)

    result_lists = []
    for p in prime_list:
        next_number = p - r_list[-1]
        if 1 < next_number <= N and next_number not in r_list:
            result_list = r_list[:]
            result_list.append(next_number)
            result_lists.append(result_list)
    return result_lists


def find_results(N):
    '''找到1~N的所有合法组合'''

    # 求出2*N以内的质数
    prime_list = []
    for i in range(2, 2 * N):
        if is_prime(i):
            prime_list.append(i)

    r_lists = [[1]]
    while len(r_lists[0]) < N:
        result_lists = []
        for r_list in r_lists:
            new_lists = add_one_number(r_list, N, prime_list)
            result_lists += new_lists  # 这里用result_lists.append(new_lists)是不正确的
        r_lists = result_lists

    end_lists = []
    for result_list in result_lists:
        if result_list[0] + result_list[-1] in prime_list:
            end_lists.append(result_list)
    return end_lists


N = int(input())
result_lists = find_results(N)
for r_list in result_lists:
    for r in r_list:
        print(r, end=' ')
    print('')
