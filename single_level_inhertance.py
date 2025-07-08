class Sales:
    sale_id = 0
    customer_id = 0
    product_id = 0
    ship_mode = 'given_ship_mode'

    def __init__(self,sale_id,customer_id,product_id,ship_mode):
        self.sale_id = sale_id
        self.customer_id = customer_id
        self.product_id = product_id    
        self.ship_mode = ship_mode

    def getSaleData(self):
        return str(self.sale_id) + '-' + self.ship_mode
    
class Product(Sales):
    product_id = 0
    category = 'given category'
    product_name = 'given product name'

    def __init__(self,product_id,category,product_name,sale_id,customer_id,ship_mode):
        super().__init__(sale_id,customer_id,product_id,ship_mode)
        self.product_id = product_id
        self.category = category
        self.product_name = product_name

    def getProductData(self):
        return str(self.product_id) + '-' + self.category + '-' + self.product_name
    
class Customer(Sales):
    customer_id = 0
    customer_name = 'given customer name'
    customer_address = 'given customer address'

    def __init__(self,customer_id,customer_name,customer_address,sale_id,product_id,ship_mode):
        super().__init__(sale_id,customer_id,product_id,ship_mode)
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_address = customer_address

    def getCustomerData(self):
        return str(self.customer_id) + '-' + self.customer_name + '-' + self.customer_address
    
sale_id = 101
customer_id = 1001
product_id = 2001
ship_mode = 'Standard Class'

p1 = Product(product_id, 'Technology', 'HTC One', sale_id, customer_id, ship_mode)


print('--- product details ---')


print('p1.product_id', p1.product_id)
print('p1.category', p1.category)
print('p1.product_name', p1.product_name)
print('p1.ship_mode', p1.ship_mode)

s1Data = p1.getSaleData()
print('s1Data', s1Data)

s2Data = p1.getProductData()
print('s2Data', s2Data)

c1 = Customer(customer_id, 'John Doe', '123 Elm St', sale_id, product_id, ship_mode)


print('--- customer details ---')


print('c1.customer_id', c1.customer_id)
print('c1.customer_name', c1.customer_name)
print('c1.customer_address', c1.customer_address)
print('c1.ship_mode', c1.ship_mode)

c1Data = c1.getSaleData()
print('c1Data', c1Data)

c2Data = c1.getCustomerData()
print('c2Data', c2Data)
    