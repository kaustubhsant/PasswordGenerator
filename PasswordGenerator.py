import sys
import random

def PasswordGenerator(pwdlen,keyword):
    rand_numbers= []
    pwd =[]
    capital_index =[]
    special_character =["!","@","#","$","%","^","&","*","(",")","_","-","+","=",".",":",";","|","~", \
                    "{","}","[","]","?"]
    if(len(keyword)<6):
        print("Please input keyword of atleast length 6")
        return
    sp_char = special_character[random.randint(0,len(special_character)-1)]
    num = int(pwdlen)- len(keyword)-1
    sp_index = random.randint(1,int(pwdlen)-1)
    n_digit = random.randint(1,len(keyword)-2)
    for i in range(0,n_digit):
        capital_index.append(random.randint(0,len(keyword)-1))
    pwdword = "".join(c.upper() if i in capital_index else c for i, c in enumerate(keyword))
    for i in range(0,num):
        if(i > 0):
            n_digit = random.randint(0,9)
            if(n_digit == rand_numbers[i-1]):
                n_digit = random.randint(0,9)
            rand_numbers.append(n_digit)
        else:
            rand_numbers.append(random.randint(0,9))
    pwd.append(pwdword[0])
    j=1
    k=0
    for i in range(1,int(pwdlen)):
        if (i== sp_index):
            pwd.append(sp_char)
        else:
            n_digit = random.randint(0,1)
            if(n_digit ==0 and j >= len(pwdword)):
                n_digit=1
            if(n_digit ==1 and k>= len(rand_numbers)):
                n_digit=0
            if(n_digit==0):
                pwd.append(pwdword[j])
                j= j+1
            else:        
                pwd.append(rand_numbers[k])
                k=k+1
    return "".join(str(c) for c in pwd)
    
if __name__ == "__main__":
    password = PasswordGenerator(sys.argv[1], sys.argv[2])
    print(password)
    