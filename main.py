from game_data import data
import random
from art import logo, vs
from clear import clear

# Choose random dict entries 1 and 2
# Print two options
# Ask user to guess A/B
# If correct - continue 
# clear console except logo - pick 2 is now pick 1, pick a random entry for pick 2
# If wrong, exit, clear console except logo, show score

def winner(first, second):
    fol1 = int(first['follower_count'])
    fol2 = int(second['follower_count'])
    if fol1 > fol2:
        return("a")
    else:
        return("b")

def main():
    playing = True
    a = random.choice(data)
    points = 0
    message = ""
    while playing:
        b = random.choice(data)
        if a == b:
            b = random.choice(data)
        top = winner(a, b)
        
        print(f"{logo}\n{message}")
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
        pick = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        if top == pick:
            points += 1
            message = "You're right! Current score: " + str(points)
            a = b
            clear()
        else:
            playing = False
            clear()
            print(logo)
            print(f"You lose! Final score: {points}")

main()