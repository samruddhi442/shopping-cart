class Product:
    def __init__(self, product_id, product_name, price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category = category

    def display_product(self):
        print(
            f"ID: {self.product_id}, Name: {self.product_name}, "
            f"Price: ₹{self.price}, Category: {self.category}"
        )


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_item_total(self):
        return self.product.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append(CartItem(product, quantity))

    def remove_product(self, product_name):
        self.items = [
            item for item in self.items
            if item.product.product_name != product_name
        ]

    def update_quantity(self, product_name, quantity):
        for item in self.items:
            if item.product.product_name == product_name:
                item.quantity = quantity

    def view_cart(self):
        print("\nShopping Cart:")
        for item in self.items:
            print(
                f"{item.product.product_name} - ₹{item.product.price} x "
                f"{item.quantity} = ₹{item.calculate_item_total()}"
            )

    def calculate_total(self):
        return sum(item.calculate_item_total() for item in self.items)

    def apply_discount(self, total):
        if total > 10000:
            discount = total * 0.15
        elif total > 5000:
            discount = total * 0.10
        else:
            discount = 0
        return discount

    def generate_invoice(self):
        subtotal = self.calculate_total()
        discount = self.apply_discount(subtotal)
        final_amount = subtotal - discount

        print("\n------ INVOICE ------")
        self.view_cart()
        print(f"\nSubtotal = ₹{subtotal}")
        print(f"Discount = ₹{discount}")
        print(f"Final Amount = ₹{final_amount}")


if __name__ == "__main__":
    p1 = Product(101, "Laptop", 50000, "Electronics")
    p2 = Product(102, "Mouse", 500, "Accessories")
    p3 = Product(103, "Keyboard", 1500, "Accessories")

    cart = ShoppingCart()
    cart.add_product(p1, 1)
    cart.add_product(p2, 2)
    cart.add_product(p3, 1)
    cart.generate_invoice()
