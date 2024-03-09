import json
import os
from apex import Apex

DATA_FOLDER = './data'
SHIPPING_ORDERS_FILE = 'shipping-orders.json'

if __name__ == '__main__':
    apex = Apex()
    products = apex.get_shipping_orders()
    products_raw = json.dumps(products, indent=2)
    with open(os.path.join(DATA_FOLDER, SHIPPING_ORDERS_FILE), 'w') as f:
        f.write(products_raw)
    print(products_raw)