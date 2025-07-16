import random

teams = ["MI", "CSK", "RCB", "KKR", "SRH", "DC", "KXIP", "RR", "GT", "LSG"]
print(*teams, sep=", ")

opp_team = random.choice(teams)
team = input("Enter your team name: ").upper()

while team not in teams:
    print("Invalid team name. Please enter a valid team name.")
    team = input("Enter your team name: ").upper()

print(f"It's {team} vs {opp_team} match!!!")
print("===================================================================")
print("Welcome to the Super Over!")
print("You have 6 balls and 1 wicket to score as many runs as possible.")
print("===================================================================")

# Toss
toss_options = ["H", "T"]
print("It's toss time!!!")
user_choice = input("Enter 'H' for Heads or 'T' for Tails: ").upper()
toss_result = random.choice(toss_options)

decision = None
opponent_decision = None

if user_choice == toss_result:
    print("Congratulations, you have won the toss!")
    decision = input("Enter 'B' to bat or 'F' to field first: ").upper()
    if decision == "B":
        print("You have chosen to bat first!")
    elif decision == "F":
        print("You have chosen to field first!")
    else:
        print("Invalid choice. Defaulting to batting first.")
        decision = "B"
else:
    print("You have lost the toss!")
    opponent_decision = random.choice(["BAT", "FIELD"])
    print(f"The opponent has chosen to {opponent_decision.lower()} first!")

print("\n===================================================================")
print(f":::::::::::::::::::::::::::::::{opp_team} VS {team}:::::::::::::::::::::::::::")
print("===================================================================")
print("Let's start the Super Over!")
print("You will face 6 balls. Let's see how many runs you can score!")


you_total = 0
opponents_total = 0

# If player bats first
if decision == "B":
    print("\nYour turn to bat first:")
    bowl = 0
    wicket = 0
    runs = 0

    while bowl < 6 and wicket < 1:
        input("Press Enter to start...")
        score = random.choice([1, 2, 3, 4, 6, "wicket", "wide", "no ball"])

        if score == "wicket":
            wicket += 1
            print("You lost a wicket!")
        elif score in ["wide", "no ball"]:
            print(f"Extra run! You scored {score}.")
            runs += 1
        else:
            runs += score
            print(f"You scored {score} runs!")
            bowl += 1

        print(f"(0.{bowl}): {runs}/{wicket}")

    you_total = runs

    print("================== second innings ==================")
    print("\nNow opponent's turn to bat!")
    bowl = 0
    wicket = 0
    runs = 0

    while bowl < 6 and wicket < 1 and runs <= you_total:
        input("Press Enter to bowl...")
        score = random.choice([1, 2, 3, 4, 6, "wicket", "wide", "no ball"])

        if score == "wicket":
            wicket += 1
            print("Opponent lost a wicket!")
            bowl += 1
        elif score in ["wide", "no ball"]:
            print(f"Extra run! Opponent scored {score}.")
            runs += 1
        else:
            runs += score
            print(f"Opponent scored {score} runs!")
            bowl += 1

        print(f"Needs {you_total + 1 - runs} runs in {6 - bowl} balls")
        print(f"(0.{bowl}): {runs}/{wicket}")

    opponents_total = runs

# If opponent bats first
elif opponent_decision == "BAT":
    print(f"\n{opp_team} is batting first!")
    bowl = 0
    wicket = 0
    runs = 0

    while bowl < 6 and wicket < 1:
        input("Press Enter to bowl...")
        score = random.choice([1, 2, 3, 4, 6, "wicket", "wide", "no ball"])

        if score == "wicket":
            wicket += 1
            print("Opponent lost a wicket!")
        elif score in ["wide", "no ball"]:
            print(f"Extra run! Opponent scored {score}.")
            runs += 1
        else:
            runs += score
            print(f"Opponent scored {score} runs!")
            bowl += 1

        print(f"(0.{bowl}): {runs}/{wicket}")

    opponents_total = runs

    print("================== second innings ==================")
    print("\nNow it's your turn to bat!")
    bowl = 0
    wicket = 0
    runs = 0

    while bowl < 6 and wicket < 1 and runs <= opponents_total:
        input("Press Enter to start...")
        score = random.choice([1, 2, 3, 4, 6, "wicket", "wide", "no ball"])

        if score == "wicket":
            wicket += 1
            print("You lost a wicket!")
            bowl += 1
        elif score in ["wide", "no ball"]:
            print(f"Extra run! You scored {score}.")
            runs += 1
        else:
            runs += score
            print(f"You scored {score} runs!")
            bowl += 1

        print(f"Needs {opponents_total + 1 - runs} runs in {6 - bowl} balls")
        print(f"(0.{bowl}): {runs}/{wicket}")

    you_total = runs

# Final Result
print("\n===================================================================")
if you_total > opponents_total:
    print(f"Congratulations! {team} wins the Super Over by {you_total - opponents_total} run(s)!")
elif opponents_total > you_total:
    print(f"Sorry! {opp_team} wins the Super Over by {opponents_total - you_total} run(s)!")
else:
    print("It's a tie! What a thrilling Super Over!")
