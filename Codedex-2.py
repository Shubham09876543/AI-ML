# 17. Enter PIN

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')


# 18. Guess Number
# Write code below 💖

guess = 0
tries = 0

while guess != 6 and tries<5:
  guess = int(input("Guess the number:  "))
  tries = tries + 1

if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')



# 19. Detention 

for i in range(101):
  print(i , "I will not use Snapchat in class")


# 20. 99 Bottles
# Write code below 💖

# String concatenation

for i in range(99,0,-1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print('Take one down, pass it around')
  print(f'{i-1} bottles of beer on the wall')

