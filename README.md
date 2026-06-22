# shopping-cart management system

from abc import ABC, abstractmethod

# ---------------------- Product Class ----------------------

class Product:
    def __init__(self, product_id, name, price, category):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__category = category

    # Getters
    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_category(self):
        return self.__category

    def display_product(self):
        print(f"ID:{self.__product_id}")
        print(f"Name:{self.__name}")
        print(f"Category:{self.__category}")
        print(f"Price: ₹{self.__price}")


# ---------------------- Cart Item ----------------------

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_item_total(self):
        return self.product.get_price() * self.quantity


# ---------------------- Discount (Inheritance & Polymorphism) ----------------------

class Discount(ABC):

    @abstractmethod
    def apply(self, total):
        pass


class ShoppingDiscount(Discount):

    def apply(self, total):

        if total > 10000:
            return total * 0.15

        elif total > 5000:
            return total * 0.10

        else:
            return 0


# ---------------------- Shopping Cart ----------------------

class ShoppingCart:

    def __init__(self):
        self.cart = []
        self.discount = ShoppingDiscount()

    # Add Product
    def add_product(self, product, quantity):

        for item in self.cart:

            if item.product.get_id() == product.get_id():
                item.quantity += quantity
                return

        self.cart.append(CartItem(product, quantity))

    # Remove Product
    def remove_product(self, product_id):

        for item in self.cart:

            if item.product.get_id() == product_id:
                self.cart.remove(item)
                print("Product Removed Successfully.")
                return

        print("Product Not Found!")

    # Update Quantity
    def update_quantity(self, product_id, quantity):

        for item in self.cart:

            if item.product.get_id() == product_id:
                item.quantity = quantity
                print("Quantity Updated.")
                return

        print("Product Not Found.")

    # View Cart
    def view_cart(self):

        if len(self.cart) == 0:
            print("\nCart is Empty")
            return

        print("\n------------ CART ------------")

        for item in self.cart:

            print(f"{item.product.get_name()} | "
                  f"Qty:{item.quantity} | "
                  f"Price:{item.product.get_price()} | "
                  f"Total:{item.calculate_item_total()}")

    # Calculate Total
    def calculate_total(self):

        total = 0

        for item in self.cart:
            total += item.calculate_item_total()

        return total

    # Apply Discount
    def apply_discount(self):

        subtotal = self.calculate_total()
        discount = self.discount.apply(subtotal)
        final = subtotal - discount

        return subtotal, discount, final

    # Generate Invoice
    def generate_invoice(self):

        subtotal, discount, final = self.apply_discount()

        invoice = "\n=========== INVOICE ===========\n"

        for item in self.cart:

            invoice += f"{item.product.get_name():12}"
            invoice += f" Qty:{item.quantity}"
            invoice += f" Price:{item.product.get_price()}"
            invoice += f" Total:{item.calculate_item_total()}\n"

        invoice += "\n------------------------------\n"
        invoice += f"Subtotal : ₹{subtotal}\n"
        invoice += f"Discount : ₹{discount}\n"
        invoice += f"Final Bill : ₹{final}\n"

        print(invoice)

        # Optional File Handling
        with open("invoice.txt", "w") as file:
            file.write(invoice)

        print("Invoice saved as invoice.txt")


# ---------------------- Main Program ----------------------

def menu():

    products = {
        1: Product(1, "Laptop", 50000, "Electronics"),
        2: Product(2, "Mouse", 500, "Accessories"),
        3: Product(3, "Keyboard", 1500, "Accessories"),
        4: Product(4, "Headphone", 2000, "Electronics"),
        5: Product(5, "Monitor", 12000, "Electronics")
    }

    cart = ShoppingCart()

    while True:

        print("\n========= SHOPPING CART =========")
        print("1. Display Products")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. Update Quantity")
        print("5. View Cart")
        print("6. Generate Invoice")
        print("7. Exit")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:

                for product in products.values():
                    print()
                    product.display_product()

            elif choice == 2:

                pid = int(input("Enter Product ID: "))
                qty = int(input("Enter Quantity: "))

                if pid in products:
                    cart.add_product(products[pid], qty)
                    print("Product Added Successfully.")
                else:
                    print("Invalid Product ID")

            elif choice == 3:

                pid = int(input("Enter Product ID: "))
                cart.remove_product(pid)

            elif choice == 4:

                pid = int(input("Enter Product ID: "))
                qty = int(input("Enter New Quantity: "))
                cart.update_quantity(pid, qty)

            elif choice == 5:

                cart.view_cart()

            elif choice == 6:

                cart.generate_invoice()

            elif choice == 7:

                print("Thank You!")
                break

            else:
                print("Invalid Choice.")

        except ValueError:
            print("Please enter valid numbers only.")

        except Exception as e:
            print("Error:", e)


menu()
