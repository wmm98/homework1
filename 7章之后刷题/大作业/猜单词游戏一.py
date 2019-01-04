
print("H A N G M A N")

HANGMAN_LIST = [
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
target_word = "cat"
guess_error = 0  # 猜错次数
guessed_letter = ['_', '_', '_']  # 记住字母缺失的位置和已经猜中的字母
result = ""  # 猜错的字母
while guess_error < len(HANGMAN_LIST) - 1:
    print(HANGMAN_LIST[guess_error])  # 打印绞刑架的形态
    print("缺失的字母：")
    print(' '.join(guessed_letter))  # 打印字母缺失的位置和已猜中字母
    g = input("输入下一个字母：")  # 接收玩家猜测的字母
    hit = False
    for i in range(len(target_word)):  # for 循环判别猜测的字母是否出现了
        if target_word[i] == g:
            guessed_letter[i] = g
            hit = True  # 出现了被猜测的字母，令 hit 为真

    # if g not in target_word:
    #
    #     print("猜错的字母是%s" % result)
    if hit:
        if '_' not in guessed_letter:
            break  # 所有字母都已经猜出来了。跳出循环。
    else:
        guess_error += 1
        result += g
        print("猜错的字母是%s" % result)

if guess_error == len(HANGMAN_LIST) - 1:
    print("真不幸，你丢命了！")
    print(HANGMAN_LIST[guess_error])
else:
    print("你猜对了！")
    print("棒棒哒！")
