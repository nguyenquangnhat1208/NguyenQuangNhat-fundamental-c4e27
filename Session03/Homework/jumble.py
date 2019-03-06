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
# import random

# word_list = ["beast","hunter","warrior","warlock","undead","goblin","druid","assassin"]

# first_quiz = random.choice(word_list)
# shuffle = list(first_quiz)
# random.shuffle(shuffle)

# correct = first_quiz

# for i in range(0,len(first_quiz)):
#     print(shuffle[i],end=' ')
# print()
# answer = input('Your answer: ')

# while True:
    # if answer == correct:
#         print('Dân chơi cờ nhân phẩm thứ thiệt =)))')
#         break
#     else:
#         print('Bạn  đã chơi cờ nhân phẩm chưa, nếu chưa hãy chơi để biết đáp án :)')
#         answer = input('Your answer: ')
