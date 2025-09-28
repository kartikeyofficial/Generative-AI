class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []
    
    def add_item(self, item, price):
        self.items.append({'item': item, 'price': price})
    
    def __str__(self):
        if not self.items:
            return f"{self.owner}'s cart is empty."
        lines = [f"{self.owner}'s Shopping Cart:"]
        total = 0
        for i, it in enumerate(self.items, start=1):
            lines.append(f"{i}. {it['item']} - ${it['price']}")
            total += it['price']
        lines.append(f"Total: ${total}")
        return "\n".join(lines)
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __contains__(self, item_name):
        return any(it['item'] == item_name for it in self.items)
    
    def __add__(self, other):
        new_cart = ShoppingCart(self.owner + ' & ' + other.owner)
        new_cart.items = self.items + other.items
        return new_cart
    
    def __iter__(self):
        return iter(self.items)


# Real-time Usage
cart1 = ShoppingCart("Deen")
cart1.add_item("Laptop", 55000)
cart1.add_item("Mouse", 800)

cart2 = ShoppingCart("Ali")
cart2.add_item("Keyboard", 1500)

# Print cart1
print(cart1)
print("Total Items in Cart1:", len(cart1))
print("First Item in Cart1:", cart1[0]['item'])
print("Laptop in Cart1?", "Laptop" in cart1)

# Merging carts
merged_cart = cart1 + cart2
print("\nMerged Cart:")
print(merged_cart)

print("\nIterating Merged Cart Items:")
for item in merged_cart:
    print(item['item'], "-", item['price'])

            