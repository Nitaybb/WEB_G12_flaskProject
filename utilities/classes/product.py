from utilities.db.db_manager import dbManager


class Product:
    def __init__(self, name=None, description=None, price=None, picture=None):
        self.name = name
        self.description = description
        self.price = price
        self.picture = picture

    @staticmethod
    def getAllProducts():
        query = "SELECT * FROM products"
        result = dbManager.fetch(query)
        data = []
        for product in result:
            p = Product(product.name, product.description, product.price, product.picture)
            data.append(p)
        return data
