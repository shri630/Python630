email = input("Enter your email: ")#g@g.in ,kambala@gmail.com
k,j,d=0,0,0 # k for space and j for upper case
if len(email) >6 :
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-3]==".") ^ (email[-4]=="."): # both must be no true or not false so so xor op
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if  i.isupper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="." or i=="_" or i=="@":
                        continue
                    else:
                        d=1        
                if k==1 or j==1 or d==1:
                    print("Invalid email_5",k,j,d) 
                else:
                    print("Valid email")           
            else:
                print("Invalid email_4")
        else:
            print("Invalid email_3") 
    else:
        print("Invalid email_2")

else:
    print("Invalid email_1")