import random

words_list = ["apple", "mango", "apricot"]
chosen_word = random.choice(words_list)
print(chosen_word)

lives = 6
place_holder = ""

word_length = len(chosen_word)

for position in range(word_length):
    place_holder += "_"

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.")
        print(f"You have {lives} lives left.")

        if lives == 0:
            game_over = True
            print("You lose")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win")
