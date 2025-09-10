# Part E: Mini Challenge

# 1. Take user's full name as input
user_name = input("Enter your full name: ")

# 2. Display the name in title case
title_case_name = user_name.title()

# 3. Display the total number of characters (excluding spaces)
char_count = len(user_name.replace(" ", ""))

# 4. Display the initials (assuming first and last name only)
name_parts = user_name.split()
initials = name_parts[0][0].upper() + name_parts[1][0].upper()

# Print the greeting message
print(f"Hello, {title_case_name}!")
print("Total characters (excluding spaces):", char_count)
print("Your initials are:", initials)
