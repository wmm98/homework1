import random

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
def input_guess(guessed_letters):
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


def play_set(target_word):
    # target_word = choice(choose_list)
    hit_letters = ['_'] * len(target_word)
    missed_letters = ''
    num_guess_failure = 0
    print("H A N G M A N")
    while num_guess_failure < len(HANGMAN_LIST) - 1:
        print(HANGMAN_LIST[num_guess_failure])
        print("当前空缺：")
        print(' '.join(hit_letters))
        # num_guess_failure = len(missed_letters)
        if num_guess_failure > 0:
             print("没猜中的字母：" + missed_letters)

        guessed_letters = ''.join(hit_letters) + missed_letters
        g = input_guess(guessed_letters)
        hit = False

        for i in range(len(target_word)):
            if target_word[i] == g:
                hit_letters[i] = g
                hit = True
        if hit:
            if '_' not in hit_letters:
                break
        else:
            missed_letters += g
            num_guess_failure += 1
    if num_guess_failure == len(HANGMAN_LIST) - 1:
        print("真不幸，你丢命了！")
        print(HANGMAN_LIST[num_guess_failure])
        print("被猜的单词是：" + target_word)
    else:
        print("你猜对了！被猜测的单词是：" + target_word)
        print("棒棒哒！")


def continue_to_play():
    '''继续玩吗？'''
    print()
    print("你要继续玩吗？(yes or no)")
    return input().lower().startswith('y')



target_words_str = "apple banana berry lemon lichee mango orange pear"
target_words_str1 = "red green black yellow blue orange white"
target_words_str2 = "pig dog cat beer duck monkey tiger lion"
target_words_str3 = "cold rain sunny warm wind hot wet"
target_words_str4 = "hello hi nihao halao hahahaha henhao"
target_words_str5 = "china australia korea england canada russia"
choose_list = [target_words_str, target_words_str1, target_words_str2,
               target_words_str3, target_words_str4, target_words_str5]



start_game = True
while start_game:
    target_words = random.choice(choose_list)
    target_words1 = target_words.split()
    target_word = random.choice(target_words1)
    if target_words == target_words_str:
        print("水果类")
    elif target_words == target_words_str1:
        print("颜色类")
    elif target_words == target_words_str2:
        print("动物类")
    elif target_words == target_words_str3:
        print("天气类")
    elif target_words == target_words_str4:
        print("见面语")
    else:
        print("国家类")
    play_set(target_word)
    start_game = continue_to_play()
print("拜拜！")