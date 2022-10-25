# Hangman

import random
import replit
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False 
lives = 6

#testing code
print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length) :
        display += "_"

while not end_of_game:
  guess = input("글자를 맞춰보세요: ").lower()
  replit.clear()
  
  if guess in display:
        print(f"이미 {guess}를 입력했습니다.")


  for position in range(word_length) :
     letter = chosen_word[position]
     if letter == guess:
       display[position] = letter

  if guess not in chosen_word:
    print(f"당신이 고른 {guess}는 단어에 없습니다.\n You lose a life")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Lose:'(")
        
  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You Win!")

  print(hangman_art.stages[lives])
