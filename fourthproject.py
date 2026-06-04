"""
email validation (using RegEx) 
emial = python@gmail.com

conditions 
# a-z = small cases
# digit = 0-9
# . and _  and @ frequwncy = 1
# . position = -2 / -3 index


"""

import re
email_condition ="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" 
user_email = input("enter your email : ")

if re.search(email_condition,user_email):  # search function in re check that user_email match with email_condition
    print("right email")

else:
    print("wrong email")
      

"""

"\"  find char in the regit  
"?"  frequency of char = 1 
"\w" = searcg special char in str  
"$" = minius indexing - $ for knowing specfic position  of char,digit and also use {} braces

completed

"""