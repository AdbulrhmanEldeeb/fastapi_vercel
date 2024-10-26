import requests

import json

# route 1
####################
# customer_data={'customer_name':"ali mohamed ahmed"}
# end_point_1='http://127.0.0.1:8000/customer/'
# response=requests.post(url=end_point_1,json=customer_data)
# print(response.status_code)

########################

# route 2
customer_id = 9
end_point_2 = f"http://127.0.0.1:8000/customers/{customer_id}"
response = requests.get(url=end_point_2, params={"customer_id": customer_id})
print(response.status_code)
print(response.json())

# route 3 --> post order
from datetime import datetime

# order_data={'customer_id':3}
# end_point_3='http://127.0.0.1:8000/order/'
# response=requests.post(url=end_point_3,json=order_data)
# print(response.status_code)
# print(response.json())

##################
# route 4 --> get customer orders
customer_id = 2

# end_point_4=f'http://127.0.0.1:8000/orders/{customer_id}'
# response=requests.get(url=end_point_4,params={'customer_id':customer_id})
# print(response.status_code)
# print(response.json())
