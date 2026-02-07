class MenuItem:
    """Models a single menu item."""

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:
    """Models the menu with available drinks."""

    def __init__(self):
        self.menu = [
            MenuItem("latte", 200, 150, 24, 2.5),
            MenuItem("espresso", 50, 0, 18, 1.5),
            MenuItem("cappuccino", 250, 50, 24, 3.0),
        ]

    def get_items(self):
        """Return a formatted string of available drink options."""
        return "/".join(item.name for item in self.menu)

    def find_drink(self, order_name):
        """Return a MenuItem if it exists, otherwise None."""
        for item in self.menu:
            if item.name == order_name:
                return item
        return None
