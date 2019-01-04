# HANGMAN_LIST = HANGMAN_LIST = [
#     '''
#  +---+
#      |
#      |
#     ===
# ''',
#     '''
#  +---+
#  o   |
#      |
#     ===
#
# ''',
#     '''
#  +---+
#  o   |
#  |   |
#      |
#     ===
# ''',
#     '''
#  +---+
#  o   |
# /|   |
#      |
#     ===
# ''',
#     '''
#  +---+
#  o   |
# /|\  |
#      |
#     ===
# ''',
#     '''
#  +---+
#  o   |
# /|\  |
# /   |
#     ===
#
# ''',
#     '''
#  +---+
#  o   |
# /|\  |
# / \  |
#     ===
# '''
# ]
#
#
# def input_guess(guessed_letters):
#     '''输入猜测的字母。把重复的猜测，非字母，非单个字母的输入，视为无效输入，要求重新输入。'''
#     while True:
#         g = input("你猜的下一个字母是：")
#         g = g.lower()  # g.lower()是把 g 变量内的字母转换为小写。非字母不予转换。
#         if len(g) != 1:
#             print("只能输入 1 个字母！")
#         elif not g.isalpha():  # .isalpha()是判别 g 变量内的字符是不是字母。
#             print("必须输入*字母*！")
#         elif g in guessed_letters:  # g 变量内的字母有在 guessed_letters 内吗？
#             print("你已经猜过这个字母。再猜一次...")
#         else:
#             return g

#
#
# # target_word = "cat"
# # hitted_letters = ['_', '_', '_']
# print("H A N G M A N")
# missed_letters = ''  # 猜错的字母
# num_guess_failure = 0
# while num_guess_failure < len(HANGMAN_LIST) - 1:
#     print(HANGMAN_LIST[num_guess_failure])
#     print("当前空缺：")
#     print(' '.join(hitted_letters))
#
#     if num_guess_failure > 0:
#         print("没猜中的字母：" + missed_letters)
#
#     guessed_letters = ''.join(hitted_letters) + missed_letters  # 玩家猜过的字母
#     g = input_guess(guessed_letters)
#     hit = False
#
#     for i in range(len(target_word)):
#         if target_word[i] == g:
#             hitted_letters[i] = g
#             hit = True
#
#     if hit:
#         if '_' not in hitted_letters:
#             break
#         else:
#             missed_letters += g
#             num_guess_failure += 1
#
# if num_guess_failure == len(HANGMAN_LIST) - 1:
#     print("真不幸，你丢命了！")
#     print(HANGMAN_LIST[num_guess_failure])
# else:
#     print("你猜对了！被猜测的单词是：" + target_word)
#     print("棒棒哒！")


HANGMAN_LIST = HANGMAN_LIST = [
    '''
 +---+
     |
     |
    ===
''',
    '''
 +---+
 o   |
     |
    ===

''',
    '''
 +---+
 o   |
 |   |
     |
    ===
''',
    '''
 +---+
 o   |
/|   |
     |
    ===
''',
    '''
 +---+
 o   |
/|\  |
     |
    ===
''',
    '''
 +---+
 o   |
/|\  |
/   |
    ===

''',
    '''
 +---+
 o   |
/|\  |
/ \  |
    ===
'''
]


def play_set(target_word):
    hitted_letters = ['_' for t in range(len(target_word))]
    return hitted_letters

def input_guess(guessed_letters):
    '''输入猜测的字母。把重复的猜测，非字母，非单个字母的输入，视为无效输入，要求重新输入。'''
    while True:
        g = input("你猜的下一个字母是：")
        g = g.lower()  # g.lower()是把 g 变量内的字母转换为小写。非字母不予转换。
        if len(g) != 1:
            print("只能输入 1 个字母！")
        elif not g.isalpha():  # .isalpha()是判别 g 变量内的字符是不是字母。
            print("必须输入*字母*！")
        elif g in guessed_letters:  # g 变量内的字母有在 guessed_letters 内吗？
            print("你已经猜过这个字母。再猜一次...")
        else:
            return g



print("H A N G M A N")
target_word = "cat"
hitted_letters = play_set(target_word)
missed_letters = ''
num_guess_failure = 0
while num_guess_failure < len(HANGMAN_LIST) - 1:
    print(HANGMAN_LIST[num_guess_failure])
    print("当前空缺：")
    print(' '.join(hitted_letters))

    if num_guess_failure > 0:
        print("没猜中的字母：" + missed_letters)

    guessed_letters = ''.join(hitted_letters) + missed_letters  # 玩家猜过的字母
    g = input_guess(guessed_letters)
    hit = False

    for i in range(len(target_word)):
        if target_word[i] == g:
            hitted_letters[i] = g
            hit = True
    if hit:
        if '_' not in hitted_letters:
            break
    else:
        missed_letters += g
        num_guess_failure += 1

if num_guess_failure == len(HANGMAN_LIST) - 1:
    print("真不幸，你丢命了！")
    print(HANGMAN_LIST[num_guess_failure])
else:
    print("你猜对了！被猜测的单词是：" + target_word)
    print("棒棒哒！")