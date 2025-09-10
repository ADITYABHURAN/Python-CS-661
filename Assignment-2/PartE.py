# Take two input strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Convert to lowercase, remove spaces, and create sets of characters
set1 = set(str1.replace(" ", "").lower())
set2 = set(str2.replace(" ", "").lower())

# Find common characters
common_chars = set1 & set2

# Find unique characters in both strings (union)
unique_chars = set1 | set2

# Find characters in one string but not the other (symmetric difference)
diff_chars = set1 ^ set2

# Print results
print("\nResults:")
print("Common characters:", common_chars)
print("Unique characters (all):", unique_chars)
print("Characters in one string but not the other:", diff_chars)
