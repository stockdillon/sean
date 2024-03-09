from datetime import date
import json
import os
from typing import List
import requests

APEX_API_KEY = 'APEX_API_KEY'


class ApexQuery:
    """
    order_date
    date	
    https://app.apextrading.com/api/v1/shipping-orders?order_date=2021-04-20 

    order_date_from
    date	
    https://app.apextrading.com/api/v1/shipping-orders?order_date_from=2021-04-20
    """

    def __init__(self, start: date, end: date) -> None:
        self.start_date = start
        self.end_date = end


class Apex:
    def __init__(self) -> None:
        self.url = "https://app.apextrading.com/api/v1/shipping-orders"
        api_key = os.environ.get(APEX_API_KEY)
        if (not api_key):
            raise ValueError(
                f'Environment variable {APEX_API_KEY} is undefined')
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Accept': 'application/json'
        }
        print('created apex client')

    def get_shipping_orders(self, query: ApexQuery = None) -> List[object]:
        response = requests.get(self.url, headers=self.headers)
        response_object = json.loads(response.text)
        return response_object
