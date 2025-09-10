# Multiplication tables of 6 and 7 using for loop
print("Table of 6:")
for i in range(1, 11):
    print(f"6 x {i} = {6 * i}")

print("\nTable of 7:")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")


# Animals list
animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile", "deer", "swan"]

# Find animals with 7 letters using while loop
seven_letter_animals = []
i = 0

while i < len(animals):
    if len(animals[i]) == 7:
        seven_letter_animals.append(animals[i])
    i += 1

print("\nAnimals with 7 letters:", seven_letter_animals)
