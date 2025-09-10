# Create an empty shopping list
shopping_list = []

# Add at least 5 items
shopping_list.extend(["milk", "bread", "eggs", "rice", "fruits"])

# Add a new item
shopping_list.append("butter")

# Print first item
print("First item:", shopping_list[0])

# Print last item
print("Last item:", shopping_list[-1])

# Print entire list
print("Entire shopping list:", shopping_list)

# Print important items (based on preference)
important_items = ["milk", "rice", "eggs"]   # You can choose based on your preference
print("Important items to buy:", important_items)

# Change an existing item (replace "bread" with "cheese")
shopping_list[1] = "cheese"

# Delete one item (remove "fruits")
shopping_list.remove("fruits")

# Print updated list
print("Updated shopping list:", shopping_list)
