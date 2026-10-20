import random
random_number = ['hello', 'pushpam', 'raj']
computer_choose = random.choice(random_number)
words = []
computer_chooses = []
life = len(computer_choose)
for word in computer_choose:
    computer_chooses.append(word)
for i in range(len(computer_choose)):
    words.append("_")
print(words)
for i in range(len(computer_chooses)):
    gusse_letter = input("Guess the letter: ")
    for i, word in enumerate(computer_chooses):
        if gusse_letter == word:
            words[i] = gusse_letter
    print(words)