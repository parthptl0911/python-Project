"""
1) generate 12 random unique tickets between 1- 100

2) divide 6 - 6 unique random tickets

3) start your game -it will give one random number

4) whoce all ticket got who will win 

"""

import random

numbers = []
while len(numbers) < 12:
    num = random.randint(1, 100)
    if num not in numbers:
        numbers.append(num)

print("\nTotal Number of tickets :")
for i in range(len(numbers)):
    print(numbers[i],end=" ")
player1 = numbers[:6]
player2 = numbers[6:]

print("\nPlayer 1's number of ticket:")
for i in range(len(player1)):
    print(player1[i], end=" ")

print("\nPlayer 2's number of ticket:")
for i in range(len(player2)):
    print(player2[i], end=" ")

while len(player1) > 0 and len(player2) > 0:
    guess = random.choice(numbers)
    print("Guess:", guess)
    if guess in player1:
        player1.remove(guess)
        numbers.remove(guess)
        print("Hit Player 1 ticket!")
        print("=====================")
    elif guess in player2:
        player2.remove(guess)
        numbers.remove(guess)
        print("Hit Player 2 ticket !")
        print("=====================")
    
if len(player1) == 0:
    print("Player 1 wins!!!")

elif len(player2) == 0:
    print("Player 2 wins!!!")
