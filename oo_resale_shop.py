from typing import Dict, Optional
from computer import Computer

class ResaleShop:
    def __init__(self):
        """Initialize an empty inventory."""
        self.inventory = {}  # Dictionary to store computers with item_id as key
        self.new_id = 0  # Unique ID for each computer

    def buy_computer(self, Computer):
        """Function adds a new computer to the inventory and assign it a unique ID."""
        item_id = self.new_id
        self.inventory[item_id] = Computer
        self.new_id += 1
        print(f"Computer bought and assigned Item ID: {item_id}")
        return item_id

    def update_price(self, item_id: int, new_price: int):
        """Function updates the price of a computer in inventory."""
        if item_id in self.inventory:
            self.inventory[item_id].update_price(new_price)
        else:
            print(f"Item {item_id} not found. Cannot update price.")

    def sell_computer(self, item_id: int):
        """Function checks if the computer being sold exists and then removes a computer from inventory."""
        if item_id in self.inventory:
            del self.inventory[item_id]
            print(f"Item {item_id} sold!")
        else:
            print(f"Item {item_id} not found. Cannot sell.")

    def refurbish_computer(self, item_id: int, new_os: str = None):
        """Function refurbishes a computer in inventory by adjusting price and updating OS if provided."""
        if item_id in self.inventory:
            self.inventory[item_id].refurbish(new_os)
        else:
            print(f"Item {item_id} not found. Cannot refurbish.")

    def print_inventory(self):
        """Prints the current inventory of computers."""
        if self.inventory:
            print("\nCurrent Inventory:")
            for item_id, Computer in self.inventory.items():
                print(f"Item ID: {item_id}, {Computer.description}, ${computer.price}")
        else:
            print("No inventory to display.")