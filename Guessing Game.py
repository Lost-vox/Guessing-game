import random

guesses = 0

print("Hey what is your name?")
yourname = input()

theNumber = random.randint(1, 10)
print('alrighty then,' + yourname + 'I have a nummber between 1 and 10 try to guess it in 5 guesses.')

while guesses < 10:
  print('Take a guess')
  guess = input()
  guess = int(guess)
  
  if guess < theNumber:
    print('Well your wrong thats too low')
    guesses += 1
  
  if guess > theNumber:
    print('Well your wrong thats too high')
    guesses += 1
    
  if guess == theNumber:
    break

 if guess == theNumber:
  guesses = str(gusses)
  print('Great you won with,' + str(guesses) + 'the number was,' + theNumber)
  
 if guess != theNumber:
  theNumber = str(theNumber)
  print('Sorry the number is actually,' + theNumber)

 #Change guesses to 10
