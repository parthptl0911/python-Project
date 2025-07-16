class Order:

    total_pizza_sold = 0
    total_pasta_sold = 0
    total_pizza_amount = 0.0
    total_pasta_amount = 0.0
    total_soft_drinks = 0
    total_bruschetta = 0
    total_brownies = 0

    #DEFAULT FOR ALL ORDERS--------------------------------------------
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.pizza_qty = 0
        self.pasta_qty = 0
        self.pizza_total = 0.0
        self.pasta_total = 0.0
        self.order_total = 0.0

    # ITEMS MENU---------------------------------
    def display_menu(self):
        print("Menu:")
        print(" 1 large pizza = 10.99 AUD")
        print(" 2 large pizzas = 20.99 AUD")
        print(" 3 large pizzas = 29.99 AUD")
        print("*** Buy 4 or more pizzas and get 1.5lt soft drink free ***")
        print(" 1 large pasta = 9.5 AUD")
        print(" 2 large pastas = 17.00 AUD")
        print(" 3 large pastas = 27.50 AUD")
        print("*** Buy 4 or more pastas and get 2 bruschetta free ***")
        print("*** Buy 4 or more pizzas and 4 or more pastas and get 2 chocco brownies ice cream free ***")


class PizzaPastaOrder(Order):
    def take_order(self):
        try:
            self.pizza_qty = int(input("Enter number of pizza order you want: "))
            self.pizza_total = self.calculate_pizza_price(self.pizza_qty)
            print(f"Your pizza order amount is: {self.pizza_total:.2f}")
            if self.pizza_qty >= 4:
                print("*** Congratulations !! 1.5lt softdrink free ***")
                Order.total_soft_drinks += 1
        except ValueError:
            print("Invalid pizza quantity entered.")

        try:
            self.pasta_qty = int(input("Enter number of pasta order you want: "))
            self.pasta_total = self.calculate_pasta_price(self.pasta_qty)
            print(f"Your pasta order amount is: {self.pasta_total:.2f}")
            if self.pasta_qty >= 4:
                print("*** Congratulations !! Get 2 bruschetta free ***")
                Order.total_bruschetta += 1
        except ValueError:
            print("Invalid pasta quantity entered.")

        if self.pizza_qty >= 4 and self.pasta_qty >= 4:
            print("*** Congratulations !! Get 2 chocco brownies ice cream free ***")
            Order.total_brownies += 1

        self.order_total = self.pizza_total + self.pasta_total
        print(f"\nTotal order for {self.customer_name}: {self.order_total:.2f}")

        # Update totals
        Order.total_pizza_sold += self.pizza_qty
        Order.total_pasta_sold += self.pasta_qty
        Order.total_pizza_amount += self.pizza_total
        Order.total_pasta_amount += self.pasta_total

    # calculates the price of pizza and pasta based on quantity
    def calculate_pizza_price(self, qty):
        if qty == 1:
            return 10.99
        elif qty == 2:
            return 20.99
        elif qty == 3:
            return 29.99
        elif qty >= 4:
            return round(10.99 * qty, 2)

    def calculate_pasta_price(self, qty):
        if qty == 1:
            return 9.50
        elif qty == 2:
            return 17.00
        elif qty == 3:
            return 27.50
        elif qty >= 4:
            return round(9.50 * qty, 2)

#final Bill of all customers orders
def print_final_summary():
    print("\=============================================================")
    print("\----------- Pizza and Pasta Bill Summary --------------")
    print("\=============================================================")

    print(f"Payment received from pizza: {Order.total_pizza_amount:.2f}")
    print(f"Payment received from pasta: {Order.total_pasta_amount:.2f}")
    print(f"Total payment received today: {Order.total_pizza_amount + Order.total_pasta_amount:.2f}")
    print(f"Number of pizzas sold: {Order.total_pizza_sold}")
    print(f"Number of pastas sold: {Order.total_pasta_sold}")
    print(f"Total pizza and pasta items sold: {Order.total_pizza_sold + Order.total_pasta_sold}")
    print(f"Number of 1.5lt soft drink bottles given: {Order.total_soft_drinks}")
    print(f"Number of bruschetta given to customers: {Order.total_bruschetta}")
    print(f"Number of chocco brownies ice creams given to customers: {Order.total_brownies}")
    print("Thank you! Bye Bye.")



def main():
    print("=================================================================")
    print(":::::::::: Welcome to Amazing Pizza and Pasta Pizzeria :::::::::::")
    print("=================================================================")

    try:
        print("\nPress 1 : Order Menu")
        print("Press 2 : Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            # First customer (no prompt)
            customer_name = input("Enter your name: ")
            order = PizzaPastaOrder(customer_name)
            print(f"Welcome, {order.customer_name}")
            order.display_menu()
            order.take_order()

            # Repeat for more customers
            while True:
                another = input("Do you want to enter order from another customer (Y/N)? ").strip().lower()
                if another == 'y':
                    customer_name = input("Enter your name: ")
                    order = PizzaPastaOrder(customer_name)
                    print(f"Welcome, {order.customer_name}")
                    order.display_menu()
                    order.take_order()
                elif another == 'n':
                    print_final_summary()
                    break
                else:
                    print("Please enter Y or N only.")
        elif choice == 2:
            print("Thank you! Visit Again.")
        else:
            print("Invalid input! Please enter 1 or 2.")
    except ValueError:
        print("Invalid input! Please enter a valid number (1 or 2).")


main()
