class MoneyMachine:
    """Handles monetary transactions."""

    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        self.profit = 0.0

    def report(self):
        """Print the current profit."""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Return total value of inserted coins."""
        print("Please insert coins.")
        total = 0

        try:
            for coin, value in self.COIN_VALUES.items():
                count = int(input(f"How many {coin}?: "))
                total += count * value
        except ValueError:
            print("❌ Invalid coin input.")
            return 0

        return round(total, 2)

    def make_payment(self, cost):
        """Return True if payment succeeds, otherwise refund."""
        money_received = self.process_coins()

        if money_received < cost:
            print("❌ Sorry, that's not enough money. Money refunded.")
            return False

        change = round(money_received - cost, 2)
        if change > 0:
            print(f"💰 Here is {self.CURRENCY}{change} in change.")

        self.profit += cost
        return True
