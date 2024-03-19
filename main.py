import random

# Ask the user for their first name
user_name = input("What is your first name? ")
print(f"Nice to meet you, {user_name}!")

# Ask the user about their shoe preference
shoe_preference = input("What shoes do you like? ")
print(f"Nice choice! {shoe_preference} is always in!")

# Ask the user for their age
user_age = int(input("How old are you? "))
print(f"{user_age} is a good age to start exploring style.")
print("I think I might know your style.")

# Ask about their favorite top
top_preference = input(f"So, {user_name}, what is your favorite top? ")
if "t-shirt" in top_preference.lower():
    print("T-shirts are classic!")
elif "sweater" in top_preference.lower():
    print("Sweaters are cozy!")
else:
    print("That's a unique choice!")

random_response = random.randint(1, 3)
if random_response == 1:
    print("Ayy, that’s lit.")
elif random_response == 2:
    print("That's in right now.")
else:
    print("Wow, so stylish!")

# Ask about their choice of bottom
bottom_preference = input("What about your choice of bottom? ")
if "jeans" in bottom_preference.lower():
    print("Jeans are versatile!")
elif "skirt" in bottom_preference.lower():
    print("Skirts are trendy!")
else:
    print("Interesting choice for bottoms!")

# Ask if there's anything else the user wants to add
additional_comments = input("Anything else you want to add? ")
if "accessories" in additional_comments.lower():
    print("Accessories can make or break an outfit!")
elif "colors" in additional_comments.lower():
    print("Colors can reflect your mood!")
else:
    print("Your style journey sounds exciting, share more next time!")

print(f"Well, {user_name}, it was awesome getting to know your style.")