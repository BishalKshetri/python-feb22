# 11/03/2026

# # Dictionaries are also mutable, meaning we can change their contents after creation.
# #  We can update existing key-value pairs or add new ones.
# a = {
#     "name": "hari",
#     "address": "Nepal",
#     "age": 1,
#     "age": 13  # Duplicate key! Only last value is kept
# }
# a["address"] = "Kathmandu"  # Update value for existing key
# a["age"] = 14  # Update value for existing key
# a["phone"] = "1234567890"  # Add new key-value pair
# print(a)

# # update() method can also be used to update multiple key-value pairs at once
# a.update({"name": "Hari Prasad", "age": 15})
# print(a)

# # other methods of dictionaries are : 
# # del() to remove a key-value pair,
# # pop() to remove a key-value pair, 
# # clear() to remove all items, 
# # get() to safely access values without KeyError, 
# # items() to get key-value pairs as tuples, and more.

# del a["phone"]  # Remove key-value pair with key "phone"
# print(a)    

# a.pop("address")  # Remove key-value pair with key "address"
# print(a)

# a.popitem()  # Remove and return an arbitrary key-value pair (last inserted in Python 3.7+)
# print(a)

# a.clear()  # Remove all items from the dictionary
# print(a)  # Output: {}

# # copying a dictionary
# a = {"name": "hari", "age": 15}
# b = a.copy()  # Create a shallow copy of dictionary a
# print(b)

# # get() method to access values safely
# print(a.get("name"))  # Output: 'hari'
# print(a.get("address"))  # Output: None (key does not exist)    
# print(a.get("address", "Not Found"))  # Output: 'Not Found' (default value if key does not exist)

# data = {
#     "name": "Hari Prasad",
#     "age": 15,
#     "address": "Kathmandu",
#     "phone": "1234567890",
#     "religion": "Hindu",
# }
# # print(data['Name'])  # Output: 'Hari Prasad'
# print(data.get('Name'))  # Output: 'Hari Prasad'


# # nested dictionaries
# user_info = {
#     "name": "Bishal Budhakshetri",
#     "age": 25,
#     "address": {
#         "city": "Kathmandu",
#         "country": "Nepal"
#     }
# }

# print(user_info.values()) 
# # Output: dict_values(['Bishal Budhakshetri', 25, {'city': 'Kathmandu', 'country': 'Nepal'}] )

# print(user_info["address"]["country"]))

user_info = {
    "name":"Bishal Budhakshetri",
    "phone":[
        {
            "type":"ntc",
            "number":982367323
        },
          {
            "type":"ncell",
            "number":984632223
        }
    ]
}

name = user_info["name"]
type1 = user_info["phone"][0]["type"]
number1 = user_info["phone"][0]["number"]   
type2 = user_info["phone"][1]["type"]
number2 = user_info["phone"][1]["number"]       

print('my name is', name, 'my',type1,'number is', number1, 'and my', type2, 'number is', number2)
