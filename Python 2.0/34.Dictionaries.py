customer = {
    "name":"John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer["age"])
print(customer["is_verified"])

customer["name"] = "Jack smith"
print(customer["name"])

customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])

print(customer.get("day", "sunday"))
