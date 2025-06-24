import random

print("Level 1: Guess the number between 1 and 100 (Unlimited Attempts)")
computer = random.randint(1, 100)

while True:
    user = int(input("Enter your guessed number: "))
    if user > computer:
        print("HINT: Guess lower number")
    elif user < computer:
        print("HINT: Guess higher number")
    else:
        print(" RIGHT GUESS !!! You passed Level 1!")
        break  

print(" Level 2: Guess the number between 1 and 50 (You have 7 attempts)")
computer = random.randint(1, 50)
level2 = False

for i in range(1, 8):
    user = int(input(f"Attempt {i}: Enter your guessed number: "))
    if user > computer:
        print("HINT: Guess lower number")
    elif user < computer:
        print("HINT: Guess higher number")
    else:
        print(" RIGHT GUESS !!! You passed Level 2!")
        level2 = True
        break

if level2:
    print("Level 3: Guess the number between 1 and 100 (You have 5 attempts)")
    computer = random.randint(1, 100)

    for j in range(1, 6):
        user = int(input(f"Attempt {j}: Enter your guessed number: "))
        if user > computer:
            print("HINT: Guess lower number")
        elif user < computer:
            print("HINT: Guess higher number")
        else:
            print(" RIGHT GUESS !!!")
            print(" CONGRATULATIONS! You passed all the levels!")
            break
    else:
        print(" You failed Level 3. Game Over.")
else:
    print(" You failed Level 2. Game Over.")
