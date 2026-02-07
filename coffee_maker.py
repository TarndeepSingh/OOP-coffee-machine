class CoffeeMaker:
    """Models the coffee machine resources and actions."""

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Print current resource levels."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Return True if enough resources exist to make the drink."""
        for item, required in drink.ingredients.items():
            if required > self.resources.get(item, 0):
                print(f"❌ Sorry, there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink):
        """Deduct resources and serve the coffee."""
        for item, amount in drink.ingredients.items():
            self.resources[item] -= amount
        print(f"☕ Here is your {drink.name}. Enjoy!")
