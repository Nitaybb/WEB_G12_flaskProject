from utilities.db.db_manager import dbManager

class Product:
    def __init__(self, product_ID=None, name=None, description=None, price=None, picture=None):
        self.product_ID=product_ID
        self.name=name
        self.description=description
        self.price=price
        self.picture=picture
