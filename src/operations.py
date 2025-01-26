from .database import Product, Movements

# Create new product
def product_create(name, category, price):
    return Product.create(name=name, category=category, price=price, current_stock=0)

# Delete product
def product_delete(id):
    query = Product.delete().where(Product.id == id)
    return query.execute()

# Show product list
def product_list():
    return list(Product.select())

# Register Buy
def register_buy(product_id, amount):
    try:
        product = Product.get(Product.id  == product_id)
        product.current_stock = product.current_stock + amount
        product.save()
        return Movements.create(product=product_id, type = 'in', amount=amount)
    
    except Product.DoesNotExist:
        print(f"Error: Producto con ID {product_id} no existe.")
        return None

# Register sale
def register_sale(product_id, amount):
    try:
        stock = product_stock(product_id)

        if amount <= stock:
            product = Product.get(Product.id == product_id)
            product.current_stock = product.current_stock - amount
            product.save()
            return Movements.create(product=product_id, type = 'out', amount=amount)
        else:
            return None    

    except Product.DoesNotExist:
        print(f"Error: Producto con ID {product_id} no existe.")
        return None
    
# Stock
def product_stock(id):
    try:
        product = Product.get_by_id(id)
        return product.current_stock
    except Product.DoesNotExist:
        print(f"Error: Producto con ID {id} no existe.")
        return 0
    except Exception as e:
        print(f"Error al obtener el stock: {e}")
        return 0
    
# Update price
def update_price_product(product_id, new_price):
    try:
        product = Product.get(Product.id == product_id)
        product.price = new_price
        product.save()
    except Product.DoesNotExist:
        return None 

# Low Stock
def list_low_stock():
    return list(Product.select().where(Product.current_stock == 0))
