import random
word_list = ["python", "programming", "language", "computer", "science"]

# ======= My Own Code ======= #

print("Word list: ", word_list)

# ======= My Own Code ======= #

# Select a random word from the list
word = random.choice(word_list)

#initiate max_no_of_incorrect_guesses variable.
# WRITE YOUR CODE HERE
max_no_of_incorrect_guesses = 6

''' Create a list of underscores that is the same length as the selected word. 
This will be used to represent the word that is being guessed,
with underscores representing unguessed letters.'''

# use list multiplication to create list of underscores.
# [list] multiplied by value

# YOUR CODE GOES HERE
curr_state = ["_"]*len(word)
# YOUR CODE ENDS HERE

# ======= My Own Code ======= #
i = 0
# ======= My Own Code ======= #

# Use a while loop to continue the game until the player runs out of guesses.
# The while loop runs until the variable max_no_of_incorrect_guesses is greater than or equal to 0.

while (max_no_of_incorrect_guesses >= 0):
  # use join() to print the current state of the game. 
  print("".join((curr_state))) # complete this line.

  # Get player's guessed letter as input
  guess = str(input("Guess a character: "))
  if not guess.isalpha() or len(guess) > 1:
      print("Please enter a single letter.")
      continue

  # Check if the player has lost the game lol
  # HINT: this will happen for which value of max_no_of_incorrect_guesses :P
  if (max_no_of_incorrect_guesses == 0):
      print("Oops! Your guesses are over. Better luck next time ^_^ Word was: ", word, "Refresh to play again.")
      break
      #print any message for the loser and the word and end the loop.

  # Check if the guess is in the word and update the list curr_state accordingly.
  if (guess in word):
      # YOUR CODE GOES HERE
      print("Correct guess! Keep going on.")
      for i in range(len(word)):
          if word[i] == guess:
              curr_state[i] = guess
      if "_" not in curr_state:
          print("Kuddos! You have guessed the word. Refresh to play again.")
          break
      # YOUR CODE ENDS HERE
  
  if (guess not in word):
      # print the corresponding hangman pic from above list. and complete this line of code.
      # You need to access the pic by defining the correct expression for index.
      # This expression will consist of length of HANGMANPICS and max_no_of_incorrect_guesses
      print("Wrong guess! Try again.",HANGMANPICS[i],"Guesses left: ",max_no_of_incorrect_guesses)
      i+=1
      # don't forget to decrement so that while loop doesn't run till infinity ;P
      max_no_of_incorrect_guesses-=1