import random

print("Welcome to Python Random Coin Tosser! xD")
input("- Press ENTER when ready to toss! -")

random_float = random.random()
if round(random_float, 2) >= 0.50:
  print(f"\nNumber is {round(random_float, 2)}, so it is heads!")
else:
  print(f"\nNumber is {round(random_float, 2)}, so it is tails!")

print("\nThank you for playing, very much! xoxo")
