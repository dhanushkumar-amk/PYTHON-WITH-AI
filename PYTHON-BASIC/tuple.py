#  same as list => order maintain then indexing , but it is immutable


trip_Summary = ("Uber go", "chennai", "airport", 450.00, "completed")
print(trip_Summary)


print(trip_Summary[1])
print(trip_Summary[-1])


for i in trip_Summary:
    print(i)

print(len(trip_Summary))

print(trip_Summary.count("chennai"))
print(trip_Summary.index("chennai"))


print(trip_Summary)

