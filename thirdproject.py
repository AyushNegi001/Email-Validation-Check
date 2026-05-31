"""
Email Validation (using String)
 
"""

email = input("enter youe Email : ") #python@gmail.com
k = 0
j = 0
d = 0
if len(email) >=15:  # check total no. of characters more then 15 or equal to 15 
    if email[0].isalpha(): # check the first letter  of gmail is alphabet
        if ("@" in email) and (email.count("@")==1):  # check the email consit of  "@" and the no. of "@" is 1
            if (email[-4] ==".") ^ (email[-3]== "."): # position of dot(.)
                for i in email:
                    if i.isspace():  #check space in the emial
                        k=1
                    elif i.isalpha():
                        continue
                    elif i.isdigit():     # check the first letter is digit or not 
                       continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1 


                if k==1 or d==1:
                    print("Wrong Emai 5")

                else:
                    print("Right Email")

            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Emiil 2")
else:
    print("Wrong Email 1 ")


