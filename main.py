from datetime import datetime, date
import json
import os
from apex import Apex, ApexQuery

DATA_FOLDER = './data'
SHIPPING_ORDERS_FILE = 'shipping-orders.json'
NUMBER_OF_DAYS_TO_QUERY = 5


def dates(days: int):
    now = datetime.now()
    start = f'{now.year}-{now.month}-{now.day - days}' # TODO: fix end-of-month scenario
    end = f'{now.year}-{now.month}-{now.day}'
    return start, end


if __name__ == '__main__':
    apex = Apex()
    start, end = dates(NUMBER_OF_DAYS_TO_QUERY)
    query = ApexQuery(start=start, end=end)
    orders = apex.get_shipping_orders(query=query)
    orders_raw = json.dumps(orders, indent=2)
    with open(os.path.join(DATA_FOLDER, SHIPPING_ORDERS_FILE), 'w') as f:
        f.write(orders_raw)
    # print(orders_raw)
    for order in orders['orders']:
        buyer_name = order['buyer']['name']
        order_total = order['total']
        print(f'Buyer Name: {buyer_name} | Total: {order_total}')
