#Dictionary:-stores keys and its values, mutable in nature, can be changed

dict1=\
    {
        "name":"Pramod",  #name=key, pramod= value
        "age":34,
        "isMale":True,
        "Address":"Bangalore"
    }
print(dict1.get("Address"))
print(dict1["Address"])
print(dict1.values())  #gives all values
print(dict1.keys())  #gives all keys

phone_book=dict(name="Amit",Age=57,Address="Delhi")
print(phone_book)   #{'name': 'Amit', 'Age': 57, 'Address': 'Delhi'}
