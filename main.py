import random 
import replit 
import hangman_art 
import hangman_words

print(hangman_art.logo) # 첫 시작 로고 불러오기

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

# 고른 알파벳이 있는 경우 -> letter 작성  
for position in range(word_length) : 
  letter = chosen_word[position] 
  if letter == guess: 
    display[position] = letter

# 고른 알파벳이 없는 경우 -> 목숨 하나 없어짐
if guess not in chosen_word: 
  print(f"당신이 고른 {guess}는 단어에 없습니다.\n You lose a life") 
  lives -= 1 
  if lives == 0: 
    end_of_game = True print("You Lose:'(")

print(f"{' '.join(display)}")

# 알파벳 다 맞춘경우 -> _ 이 다 사라질 때 -> 이김
if "_" not in display: 
  end_of_game = True 
  print("You Win!")

print(hangman_art.stages[lives])
