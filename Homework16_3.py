class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    # Если продукт уже есть, обновляю его количество
    def add(self, product, amount):
        if amount <= 0:
            raise ValueError("Количество должно быть положительным")

        if product.name in self.products:
            self.products[product.name]['quantity'] += amount
        else:
            #Скидочка 30%
            self.products[product.name] = {
                'product': product,
                'quantity': amount,
                'price': product.price * 1.3
            }

    def set_discount(self, identifier, percent, identifier_type='name'):
        if not (0 <= percent <= 100):
            raise ValueError("Процент скидки должен быть от 0 до 100")

        for product_name, info in self.products.items():
            product = info['product']
            if (identifier_type == 'name' and product.name == identifier) or \
                    (identifier_type == 'type' and product.type == identifier):
                info['price'] = product.price * 1.3 * (1 - percent / 100)

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError(f"Товар '{product_name}' не найден в магазине")

        product_info = self.products[product_name]
        if product_info['quantity'] < amount:
            raise ValueError(f"Недостаточно товара '{product_name}' для продажи {amount} единиц")

        sale_value = product_info['price'] * amount
        self.income += sale_value
        product_info['quantity'] -= amount
        if product_info['quantity'] == 0:
            del self.products[product_name]

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(info['product'].name, info['quantity'], info['price']) for info in self.products.values()]

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError(f"Товар '{product_name}' не найден в магазине")
        product_info = self.products[product_name]
        return product_info['product'].name, product_info['quantity']


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()
s.add(p, 10)
s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
assert s.get_income() == 1.95 * 10
