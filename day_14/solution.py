from art import logo, vs
from game_data import data
import random
"""What I got wrong on my solution/things to check on:
-I initially thought that I was actually going to have to make an instagram developer account. But it gives you basically mock API output. Oops
-I set myguess to catch uppercase letters and not catch any type of letter. [Not fully wrong, but YMMV.]
-The game repeats the second option when the user gets it right, so you need to pull from the previous guess.
-Check if the first and second random options are the same.
-I just have to take it slower. The "correct solution" has an additional function but I don't think that's needed for this program.
-Also, note this needs to be in the same folder as the sample stuff in order to work. I am not copying those imports here."""
person_b = random.choice(data)
right = True
score = 0
print(logo)

while right:
    person_a = person_b
    person_b = random.choice(data)
    while person_a == person_b:
        person_b = random.choice(data)
    print(f"Compare A: {person_a["name"]}, a {person_a["description"]}, from {person_a["country"]}."
          f"{vs}"
          f"Against B: {person_b["name"]}, a {person_b["description"]}, from {person_b["country"]}.")
    myguess = input("Who has more followers? Type 'A' or 'B':   ").lower()
    if check_correct(person_a["follower_count"], person_b["follower_count"], myguess):
        score += 1
        print("\n" * 20, logo)
        print(f"You're right! Current score: {score}")
    elif person_b["follower_count"] > person_a["follower_count"] and myguess == "b":
        score += 1
        print("\n" * 20, logo)
        print(f"You're right! Current score: {score}")
    else:
        print("\n" * 20, logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        right = False