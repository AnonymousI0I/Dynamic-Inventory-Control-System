def main():
    items = []
    prices = []
    done = False
    
    while not done:
        user_input = input("Enter 'add' to add an item, 'delete' to delete an item, or 'checkout' to finish: ").lower()
        
        if user_input == "add":
            add_item(items, prices)
        elif user_input == "delete":
            delete_item(items, prices)
        elif user_input == "checkout":
            done = True
        else:
            print("Invalid input. Please try again.")
    
    display_cart(items, prices)
    subtotal = calculate_subtotal(prices)
    tax_rate = 0.078
    total = subtotal + (subtotal * tax_rate)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total with tax: ${total:.2f}")

def add_item(items, prices):
    new_item = input("Enter the name of the item: ")
    while True:
        try:
            new_price = float(input("Enter the price of the item: "))
            break  # Exit the loop if successfully converted to float
        except ValueError:
            print("Invalid price entered. Please enter a numeric value.")
    
    items.append(new_item)
    prices.append(new_price)

def delete_item(items, prices):
    item_to_delete = input("Enter the name of the item to delete: ")
    
    if item_to_delete in items:
        index = items.index(item_to_delete)
        items.pop(index)
        prices.pop(index)
        print("Item removed successfully.")
    else:
        print("Item not found.")

def display_cart(items, prices):
    for item, price in zip(items, prices):
        print(f"Item: {item}, Price: ${price:.2f}")

def calculate_subtotal(prices):
    return sum(prices)

if __name__ == "__main__":
    main()
