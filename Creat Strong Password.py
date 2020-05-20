#This Script To Create a Very strength Password
import random

mix_c = "AB1CDEFGHI2JKLMN7OP3QRS4TUV8WX5YZ#@*+6-_&!0?%9;/[\]^`{|}~"
lower_mix_c = mix_c.lower()
all_c = mix_c + lower_mix_c
list_1 = []

agian = "Y"
while agian == "Y":
    try:
        Len_pass = int(input('\n[+]Enter how length of the password you want : '))
        if type(Len_pass) == int:
            while len(list_1) < Len_pass:
    
                i = random.choice(all_c)
                list_1.insert(0,i)
    
                if len(list_1)>= Len_pass:
                    strength_password = ''.join(list_1)
                    print(f"\n[-]Your Password is : {strength_password}")
                    break
    

       
    except ValueError:
    
        print('#' * 60)
        print('[-] Please Enter a Digit Number!')
        print('#' * 60)
    finally:
        agian = input('\n[+]Want to use again [Y/N] ? : ').capitalize()
        if agian != "Y":
            print('Good bye!')
            break

input('\nEntre To exit')
