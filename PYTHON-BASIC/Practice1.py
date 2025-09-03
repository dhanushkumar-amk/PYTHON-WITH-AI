
import sys

fullName =sys.argv[1]

email = fullName.lower().replace(' ', '.') + "@gmail.com"


print( " Your name : ",fullName)
print(" Your email address is : ",email)
