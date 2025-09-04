
setExample = {"hello", "hello", "world"}
print(setExample)

# union set

set1 = {"hello", "helloWorld", "world"}
set2 = {"kumar", "dhanush", "world"}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))


set1.add("sanjay")
print(set1)

set1.remove("hello")
print(set1)

for item in set1:
    print(item)



