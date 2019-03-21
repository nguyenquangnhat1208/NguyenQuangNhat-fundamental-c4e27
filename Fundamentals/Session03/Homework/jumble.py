import random
Dictionary = ["spotify","football","autochess","developer","instagram"]
jumble = True
words = random.choice(Dictionary)
n = len(words)
num_list = list(range(0,n))
random.shuffle(num_list)
while jumble == True: 
    for i in range(0,n):
        print(words[num_list[i]],end=" ")
    print()
    Your_guess = input("Guess the word: ")
    if Your_guess == words:
        print("Bingo")
        jumble = False
    else:
        print("Incorrect. Try again")

