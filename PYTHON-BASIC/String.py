a = "dhanush kumar"

print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.split())
print(len(a))

print("===============")


mobile_no = "123456789"
maskedNumber1  = mobile_no[2:]
maskedNumber2  = mobile_no[-1]
print(maskedNumber1)
print(maskedNumber2)


print("=================")

promo = "Hello world msg"
if "world" in promo:
    print("Is present")
else:
    print("Is not present")

print("===================")
hello = f"Hello, {maskedNumber1}"
print(hello)


hello = """hiii"""
print(hello)