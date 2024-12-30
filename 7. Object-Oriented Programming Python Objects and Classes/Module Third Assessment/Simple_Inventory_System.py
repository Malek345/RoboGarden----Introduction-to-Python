class Product:
    """
    Class to represent a product with attributes and methods.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """
        Display product information.
        """
        print(f"Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}")

    def update_quantity(self, amount):
        """
        Update the product's quantity. Positive for restocking, negative for selling.
        """
        self.quantity += amount
        if amount > 0:
            print(f"{amount} units of '{self.name}' added to stock.")
        elif amount < 0:
            print(f"{-amount} units of '{self.name}' sold.")
        print(f"Updated quantity of '{self.name}': {self.quantity}")

    def total_value(self):
        """
        Calculate the total value of the product in inventory.
        """
        return self.price * self.quantity


class Inventory:
    """
    Class to represent an inventory system.
    """
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        """
        Add a new product to the inventory.
        """
        product = Product(name, price, quantity)
        self.products.append(product)
        print(f"Product '{name}' added to inventory.")

    def display_inventory(self):
        """
        Display all products in the inventory.
        """
        if not self.products:
            print("The inventory is empty.")
        else:
            print("Inventory:")
            for product in self.products:
                product.display_info()
            print("-" * 40)

    def calculate_total_value(self):
        """
        Calculate and return the total value of all products in the inventory.
        """
        total_value = sum(product.total_value() for product in self.products)
        print(f"Total Inventory Value: ${total_value:.2f}")
        return total_value


def main():
    # Create the inventory system
    inventory = Inventory()

    # Add products to the inventory
    inventory.add_product("Laptop", 1000.00, 10)
    inventory.add_product("Smartphone", 500.00, 20)
    inventory.add_product("Headphones", 50.00, 100)

    # Display inventory
    inventory.display_inventory()

    # Update the quantity of a product
    laptop = inventory.products[0]  # Get the Laptop product
    laptop.update_quantity(-2)  # Sell 2 laptops
    laptop.update_quantity(5)   # Restock 5 laptops

    # Display updated inventory
    inventory.display_inventory()

    # Calculate total inventory value
    inventory.calculate_total_value()

main()
