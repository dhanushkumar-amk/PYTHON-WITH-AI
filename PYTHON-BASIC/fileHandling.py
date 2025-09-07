# file = open('Notes.txt', 'w')
# file.write("\n i am dhanushkumar \n")
# file.close()


with open('Notes.txt', 'r') as file:
    for line in file:
        print(line.strip())


