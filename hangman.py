# Write your code here
import random

word_list = ['javascript', 'java', 'kotlin', 'python']
valid_entries = set('abcdefghijklmnopqrstuvwxyz')  # check for only lowercase alphabet characters

print('H A N G M A N')
while True:  # game loop
    play_quit = input('Type "play" to play the game, "exit" to quit: ')
    if play_quit == 'exit':
        break
    elif play_quit != 'play':
        continue
    tries = set()  # set to keep entered characters
    count = 8  # number of tries the player gets
    choice = random.randint(0, 3)  # random choice between 0 and 3
    word = word_list[choice]  # choose the word to be guessed this round
    hint = list('-' * len(word))  # this list starts with the length of the word in dashes, and gets updated with right guesses
    while count > 0:
        cur_answer = ''.join(hint)
        print("\n" + cur_answer)
        guess = input('Input a letter: ')
        if len(guess) != 1:
            print('You should input a single letter') 
            continue
        elif guess not in valid_entries:
            print('It is not an ASCII lowercase letter')
            continue
        elif guess in tries:
            print('You already typed this letter')
            continue
        elif guess not in word:
            print('No such letter in the word')
            count -= 1
            tries.add(guess)  # add the guess to the set of tried characters
            continue
        elif guess in word:
            for j in range(len(word)):  # check each letter in the chosen word for the guess
                if guess == word[j]:
                    hint[j] = guess
            tries.add(guess)
        if cur_answer == word:
            print('You guessed the word ' + word)
            print('You survived!')
            break
    else:  # while ... else loop, if no more guesses left, game over!
        print('You are hanged!')
