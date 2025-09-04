numberList = [3,-12,3,4,5, 11, 11]


# List methods

print(numberList)
print(numberList[0])            # indexinprint(numberList[-3]-1)           # reverse Indexing

numberList.append("10")
print("After adding numbers to list")
print(numberList)

print(numberList.pop())


numberList.insert(2, 11)
print(numberList)

print(numberList.count(11))

numberList.remove(11)           # used to particular element
print(numberList)

numberList.reverse()
print(numberList)

numberList.sort()
print(numberList)


# list slicing
print("====================")

stringList = ["hello", "world", "!", "!"]
print(stringList[3:])
print(stringList[-3:-1])



print("================ String Iteration ============")
stringList = ["hello", "world", "!", "!"]
# List iteration

for string in stringList:
    print(string)


# Check if element present or not
if "world" in stringList:
    print("present")
else:
    print("not present")

stringList[2] = "Hello world"
print(stringList)


print("======= enumurator class ======")

locationList = ["Coimbatore", "Chennai", "Mumbai"]
for i, location in enumerate(locationList):
    print(f"location {i + 1} : {location}")

