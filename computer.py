class Computer:
    def __init__(self, description: str,
                 processor_type: str,
                 hard_drive_capacity: int,
                 memory: int,
                 operating_system: str,
                 year_made: int,
                 price: int):
        """Initializes a Computer object with its attributes."""
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def update_price(self, new_price: int):
        """Updates the price of the computer."""
        self.price = new_price
        print(f"Updated price: ${self.price}")

    def update_os(self, new_os: str):
        """Updates the OS."""
        self.operating_system = new_os
        print(f"Updated OS: {self.operating_system}")

    def refurbish(self, new_os: str = None):
        """Refurbishes the computer by adjusting price and optionally updating the OS."""
        if self.year_made < 2000:
            self.price = 0  # Too old to sell
        elif self.year_made < 2012:
            self.price = 250  # Discounted price for older computers
        elif self.year_made < 2018:
            self.price = 550  # Moderate discount
        else:
            self.price = 1000  # Recent models

        if new_os:
            self.update_os(new_os)

        print(f"Refurbished! New price: ${self.price}")

    def __str__(self):
        """String representation for easy debugging and printing."""
        return (f"{self.description} ({self.year_made}) - {self.processor_type}, "
                f"{self.memory}GB RAM, {self.hard_drive_capacity}GB HDD, {self.operating_system}, "
                f"Price: ${self.price}")