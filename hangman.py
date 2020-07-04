import random

def hangman():
    word_list = ["caaat", "cat", "dog"]
    word = word_list[random.randint(0,2)]
    wrong = 0
    stages = ["",
              "__________         ",
              "|        |         ",
              "|        ○         ",
              "|       /|\        ",
              "|       / \        ",
              "|                  "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマン")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("you loose! ans. {}.".format(word))

hangman()


