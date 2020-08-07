import random

def random_word():
    """Returns random word."""
    file = 'txt_files/sowpods.txt'
    words = []
    with open(file) as f:
        words = f.readlines()
    return random.choice(words).strip()

random_word = random_word()
random_word = random_word.upper()
char_list = list(random_word)
len_word = len(char_list)
list_blank = []
for num in range(len_word):
    list_blank.append('_')
print(' '.join(list_blank))

num_guesses = 6
guesses = []
print(f"You have {num_guesses} left.")
while True:
    guess = input("Guess what letter is in this word: ")
    guess = guess.upper()
    if guess not in guesses:
        num_guesses -= 1
        guesses.append(guess)
        if guess in char_list:
            indices = [i for i, x in enumerate(char_list) if x == guess]
            num_indices = len(indices)
            for num in range(num_indices):
                list_blank[indices[num]] = guess
        else:
            print(f"{guess} is not in this word. Please try again.")
    else:
        print(f"You've already guessed '{guess}'. Please try again.")
        continue
    
    print(' '.join(list_blank))
    if '_' not in list_blank:
        print(f"Congratulations, you guessed the word '{random_word}' correctly.")
        break
    elif num_guesses == 0:
        print("You lose. You used up all 6 guesses. The word was "
            f"{random_word}.")
        break
    print(f"You have {num_guesses} guesses left.")