from apps.products.models import Product, ProductLog


class ProductUploadMixin(object):
    def __init__(self, data):
        self.data = data

    def run(self):
        self.__load_multiple_products()

    def __load_multiple_products(self):
        products_list = []
        
        for product in self.data:
            products_list.append(
                Product(
                    name=product["name"], 
                    unit_price=product["unit_price"], 
                    quantity=product["quantity"]
                )
            )

        products = Product.objects.bulk_create(products_list)
        self.product_log_creator(products)

    
    def product_log_creator(self, products):
        for product in products:
            ProductLog.objects.create(
                product=product.name,
                action="New Product Added",
                quantity=product.quantity
            )