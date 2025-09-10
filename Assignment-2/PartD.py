# Create an empty dictionary for inventory
inventory = {}

# Store first product details
inventory["product1"] = {
    "Product Name": "Mobile phone",
    "Product Quantity": 5,
    "Product Price": 70000,
    "Product Release Year": 2025
}

# Store second product details
inventory["product2"] = {
    "Product Name": "Laptop",
    "Product Quantity": 10,
    "Product Price": 25000,
    "Product Release Year": 2025
}

# Display inventory
print("Initial Inventory:")
print(inventory)

# Update release year of second product to 2026
inventory["product2"]["Product Release Year"] = 2026

# Check and delete release years if present
for key in ["product1", "product2"]:
    if "Product Release Year" in inventory[key]:
        del inventory[key]["Product Release Year"]

# Display updated inventory
print("\nUpdated Inventory:")
print(inventory)
