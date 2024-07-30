# Advanced Inventory Cart Manager

This Python script provides a comprehensive solution for managing a shopping cart with advanced inventory control. The main functionalities include:

1. Adding items to the cart.
2. Deleting items from the cart.
3. Displaying the current cart contents.
4. Calculating the subtotal and total cost with tax.

## Features

- **Add Items**: Add items and their prices to the cart.
- **Delete Items**: Remove items from the cart.
- **Display Cart**: View the current items and their prices in the cart.
- **Calculate Total**: Compute the subtotal and total cost including tax.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/AnonymousI0I/Dynamic-Inventory-Control-System.git
    cd Dynamic-Inventory-Control-System
    ```

2. **Ensure Python 3.x is installed on your machine**.

## Usage

1. **Run the script**:

    ```bash
    python Dynamic Inventory Control System.py
    ```

2. **Follow the on-screen prompts to add, delete, or checkout items**:

### Adding Items

- You will be prompted to enter the name and price of the item.
- The program will add the item to the cart.

    Example:

    ```
    Enter 'add' to add an item, 'delete' to delete an item, or 'checkout' to finish: add
    Enter the name of the item: Apple
    Enter the price of the item: 1.5
    ```

### Deleting Items

- You will be prompted to enter the name of the item to delete.
- The program will remove the item from the cart if it exists.

    Example:

    ```
    Enter 'add' to add an item, 'delete' to delete an item, or 'checkout' to finish: delete
    Enter the name of the item to delete: Apple
    ```

### Checking Out

- When you are done adding and deleting items, enter 'checkout' to finish.
- The program will display the cart contents, subtotal, and total cost with tax.

    Example:

    ```
    Enter 'add' to add an item, 'delete' to delete an item, or 'checkout' to finish: checkout
    Item: Apple, Price: $1.50
    Subtotal: $1.50
    Total with tax: $1.62
    ```

## Code Overview

### Function Descriptions

#### `add_item(items, prices)`

Adds a new item and its price to the cart.

- **Parameters**:
  - `items` (list): The list of item names.
  - `prices` (list): The list of item prices.

#### `delete_item(items, prices)`

Deletes an item from the cart.

- **Parameters**:
  - `items` (list): The list of item names.
  - `prices` (list): The list of item prices.

#### `display_cart(items, prices)`

Displays the current contents of the cart.

- **Parameters**:
  - `items` (list): The list of item names.
  - `prices` (list): The list of item prices.

#### `calculate_subtotal(prices)`

Calculates the subtotal of the items in the cart.

- **Parameters**:
  - `prices` (list): The list of item prices.
- **Returns**:
  - `float`: The subtotal of the items.

#### `main()`

Handles user input and orchestrates the workflow of the program.

- Prompts the user to add or delete items or checkout.
- Displays the cart contents, subtotal, and total cost with tax.

### Example Workflow

When you run the program, you will see prompts like this:

Enter 'add' to add an item, 'delete' to delete an item, or 'checkout' to finish: add
Enter the name of the item: Apple
Enter the price of the item: 1.5
Enter 'add' to add an item, 'delete' to delete an item, or 'checkout' to finish: checkout
Item: Apple, Price: $1.50
Subtotal: $1.50
Total with tax: $1.62

## Contribution

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.
