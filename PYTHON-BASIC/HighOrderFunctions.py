
# def build_email(userName, providers):
#     if providers == 'gmail':
#         return  f"{userName}@gmail.com"
#     elif providers == 'yahoo':
#         return f"{userName}@yahoo.com"
#     elif providers == 'outlook':
#         return f"{userName}@outlook.com"
#     elif providers == 'mail':
#         return f"{userName}@mail.com"
#     else:
#         return f"{userName}@example.com"
#
# print(build_email('dhanushkumar', 'gmail'))
# print(build_email('Arun', 'outlook'))
# print(build_email('Sanjay', '''i don't know'''))



def gmail_email(userName, domain="gmail"):
    return userName + "@" + domain + ".com"

def yohoo_email(userName, domain="yohoo"):
    return userName + "@" + domain + ".com"

def outlook_email(userName, domain="outlook"):
    return userName + "@" + domain + ".com"

def hotmail_email(userName, domain="hotmail"):
    return userName + "@" + domain + ".com"

# higher order function

def build_email(userName, email_function):
    return email_function(userName)

print(build_email("dhanushkumar", yohoo_email))