import random

guesses = 0

print("Hey what is your name?")
yourname = input()

theNumber = random.randint(1, 10)
print('alrighty then,' + yourname + 'I have a nummber between 1 and 10 try to guess it in 5 guesses.')

while guesses < 5:
  print('Take a guess')
  guess = input()
  guess = int(guess)
  
  guesses = guesses + 1
  
  if guess < theNumeber:
    print('Thats too low')
    
