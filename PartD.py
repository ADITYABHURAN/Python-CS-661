# Part D: String Operations

# 1.Create variable
course = "Graduate Python Programming"

# 1. Print in all uppercase and lowercase
print("Uppercase:", course.upper())
print("Lowercase:", course.lower())

# 2. Extract and print the first word and the last word
words = course.split()  # split string into list of words
first_word = words[0]
last_word = words[-1]
print("First word:", first_word)
print("Last word:", last_word)

# 3. Count how many times the letter "a" appears
count_a = course.count("a")
print("The letter 'a' appears", count_a, "times.")

# 4. Replace "Graduate" with "Advanced"
new_course = course.replace("Graduate", "Advanced")
print("Updated string:", new_course)

# 2. Given string
text = " Python is powerful and readable! "

# 1. Strip leading and trailing spaces
stripped_text = text.strip()
print("Stripped text:", stripped_text)

# 2. Split the string into a list of words
words_list = stripped_text.split()
print("List of words:", words_list)

# 3. Join the list back into a single string separated by hyphens (-)
joined_text = "-".join(words_list)
print("Hyphen-joined text:", joined_text)
