# not in course 
# requests
# method

# 1. GET, POST
# response
# status code

# install package : after activating venv, "pip install requests"

import requests

url = "https://www.onlinekhabar.com/smtm/home/trending"

r = requests.get(url) # can be used in both positional or keyword argument
if r.status_code == 200:
    print("success")
    data = r.json()['response']
    print(type(data))
    # single_data = data[0]
    # print(single_data['ticker_name'])
    # using loop now for all
    for i in data:
        if float(i['latest_price']) <= 450:
            print(i['ticker_name'], i['latest_price'], i['percentage_change'])
    # print(r.text) # it will give html, 
else:
    print("something went wrong")