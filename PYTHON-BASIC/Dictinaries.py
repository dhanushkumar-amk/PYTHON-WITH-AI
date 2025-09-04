
myDetails = {
    "name" : "dhanushkumar",
    "age" : 21,
    "address" : {
        "city" : "Coimbatore",
        "country" : "India",
        "street" : {
            "area" : "north street",
            "city" : "amk"
        }
    },
    "designation" : "developer"
}

print(myDetails)

print(myDetails["name"])
print(myDetails["age"])

print(myDetails["address"]["street"]["city"])


print(myDetails.values())
print(myDetails.keys())

print(myDetails.get("address").get("street").get("area"))

print("============= Iteration =================")
for key, value in myDetails.items():
    print(f"{key}: {value}")



myDetails.update({"age": 20})
print(myDetails)