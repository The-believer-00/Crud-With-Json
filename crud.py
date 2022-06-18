# ## C-R-U-D // WITH JSON

import json
import re

# ## Intro start//
def intro():
    print("Welcome to Accounts:: \n1.Sign up\n2.Log in\n3.Exit\n")
    opt = int(input('enter your option number: '))
    if opt == 1:
        sign_me()
    elif opt == 2:
        log_me()
    elif opt == 3:
        exit()
    else:
        print("Invalid option: ")
        intro()

# ## SignUp//
def sign_me():
    name = input('enter your full name: ')
    age = int(input('enter your age: '))
    code = input("enter your phone number code: ")
    mob_no = int(input('enter phone number: '))
    mobile_no = mobile_num(mob_no,code)
    mail = input('enter your email address: ')
    email = valid_mail(mail)
    password = input('enter your password: ')
    pwrd = strong_pwrd(password)

    with open('crud_details.json','a+') as data:
        if data.read() == "":
            accounts_data = []
        else:
            data.seek(0)
            accounts_data = json.load(data)
        if len(accounts_data) >0:
            for dict in accounts_data:
                if mobile_no == dict["mobile.no"] or email == dict["email"]:
                    print("account with this Email and Number already exist: ")
                    intro()
                else:
                    accounts_data.append({"name":name,"age":age,"mobile.no":mobile_no,"email":email,"password":pwrd})
                    print("your account is successfully created:: ")
                    with open('crud_details.json','w') as data:
                        json.dump(accounts_data,data,indent=4)
                        print("your data is saved:: ")
                    intro()
        else:
            accounts_data.append({"name":name,"age":age,"mobile.no":mobile_no,"email":email,"password":pwrd})
            print("your account is successfully created:: ")
            with open('crud_details.json','w') as data:
                json.dump(accounts_data,data,indent=4)
                print("your data is saved:: ")
            intro()

# ## LogIn//
def log_me():
    unid = input("enter user name: ")
    pss = input("enter your password: ")

    with open('crud_details.json','r') as data:
        account_data = json.load(data)
        for dict in account_data:     
            if unid in dict.values() and pss in dict.values():
                print('---------->Login successfully: ')
                opt = int(input("what you wanna do with your data:-\n1.Read\n2.Update\n3.Delete\n4.Delete Account\n5.Create\n6.Exit\n"))
                if opt == 1:
                    print(dict)
                    intro()
                elif opt == 2:
                    upd = my_update(dict)
                    dict = upd
                    with open('crud_details.json','w') as Data:
                        json.dump(account_data,Data,indent=4)
                        print("your data is saved:: ")
                    intro()
                elif opt == 3:
                    dld = my_delete(dict)
                    dict = dld
                    with open('crud_details.json','w') as Data:
                        json.dump(account_data,Data,indent=4)
                        print("your data is saved:: ")
                    intro()
                elif opt == 4:
                    i = account_data.index(dict)
                    account_data.pop(i)
                    with open('crud_details.json','w') as Data:
                        json.dump(account_data,Data,indent=4)
                        print("your account is been deleted:: ")
                    intro()
                elif opt == 5:
                    crd = my_create(dict)
                    dict = crd
                    with open('crud_details.json','w') as Data:
                        json.dump(account_data,Data,indent=4)
                        print("your data is saved:: ")
                    intro()
                elif opt == 6:
                    intro()
                else:
                    print('Invalid input: ')
                intro()

            elif unid in dict.values() and pss not in dict.values():
                    print('invalid password; ')
                    break
            elif unid  not in dict.values() and pss in dict.values():
                print('invalid name: ')
                break
        print('account not found: ')
        intro()

# ## Valid Email checker//
def valid_mail(email_address):
    email_cond = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    if re.search(email_cond,email_address):
        return email_address
    else:
        print('invalid email.')
        email = input('enter your email address: ')
        return valid_mail(email)

# ## mobile number//
def mobile_num(num,code):
    num = str(num)
    if len(num) == 10 and '+' in code and len(code) <=3:
        code+=num
        return code
    else:
        print("invalid phone number: ")
        code = input("enter your phone number code: ")
        mob_no = input('enter phone number: ')
        return mobile_num(mob_no,code)

# ## Strong password//
def strong_pwrd(pwrd):
    special_chr = '@^&*()#%$!+-'
    d,l,u,sp, = 0,0,0,0
    if len(pwrd)<8 or len(pwrd)>16:
        print('invalid password:\nlength of your password must be greater than 7 and less than 16: ')
        pwrd = input('create password: ')
        strong_pwrd(pwrd)
    for i in pwrd:
        if i.isdigit():
            d+=1
        if i.islower():
            l+=1
        if i.isupper():
            u+=1
        if i in special_chr:
            sp+=1
    if d>=1 and l>=1 and u>=1 and sp>=1:
        print('Password Created: ')
        return pwrd
    else:
        print("invalid password:\npassword must contain a capital letter-small letter_digit_special characters(@^&*()#%$!+-)")
        pwrd = input('create password: ')
        return strong_pwrd(pwrd)

# ## Update data//
def my_update(dict):
    opt = int(input("You really want to Update your data:\n0.NO\n1.YES\n"))
    if opt:
        c =1
        for i in dict.keys():
            print(str(c)+i)
            c+=1
        n = int(input("how many items you wanna update: "))
        ele = []
        print("--Give one by one: ")
        for j in range(n):
            opt = (input("what you wanna update:-"))
            ele.append(opt)
        for i in ele:
            if i in dict:
                if i == "mobile.no":
                    code = input("enter your phone number code: ")
                    new_val = input(("enter: ",i))
                    s = mobile_num(new_val,code)
                    dict[i] = s
                elif i == "email":
                    new_val = input(("enter: ",i))
                    s = valid_mail(new_val)
                    dict[i] = s
                elif i == "password":
                    new_val = input(("enter: ",i))
                    s = strong_pwrd(new_val)
                    dict[i] = s
                else:
                    new_val = input(("enter your data for: ",i))
                    dict[i] = new_val
            else:
                print("Check your data-----Invalid request: ")
                my_update(dict)
        return dict
    else:
        intro()

# ## Delete data//
def my_delete(dict):
    opt = int(input("You really want to delete your data:\n0.NO\n1.YES\n"))
    if opt:
        c =1
        for i in dict.keys():
            print(str(c)+i)
            c+=1
        n = int(input("how many items you wanna delete: "))
        ele = []
        for j in range(n):
            opt = (input("what you wanna update:-"))
            ele.append(opt)
        for j in ele:
            if j in dict:
                 del dict[j]
            else:
                print("Check your data-----Invalid request: ")
                my_delete(dict)
        return dict
    else:
        intro()
    
# ## Create data//
def my_create(dict):
    opt = int(input("You really want to Create your data:\n1.YES\n2.NO\n"))
    if opt == 1:
        while True:
            opt = int(input("1.Add\n2.Exit\n"))
            if opt == 2:
                break
            elif opt == 1:
                key = input("what you wanna add to your data: ")
                value = input("enter your data for: ")
                dict[key] = value
            else:
                print("Invalid request: ")
                my_create(dict)
        return dict
    elif opt == 2:
        intro()
    else:
        print("Invalid request: ")
        my_create(dict)

intro()
