

username=input("Enter Username : ")
last_three_passwords=[]

for i in range(3):
    last_three_password=input("Enter last_three password :")
    last_three_passwords.append(last_three_password)

flag=False
def three_consecutive_character(password,name):
    for i in range(len(password)-2):
        if(password[i:i+3] in name):
            return False
    return True

def same_chr_repeated_more_than_3_times(password):
    for i in range(len(password)):
        count=0
        for j in range(i+1,i+4):
            if(j<len(password) and password[i]==password[j]):
                count+=1
            else:
                break
        if(count>=3):
            return False
    return True

def validate_password(password,name,passwords):
    if(len(password)<10):
        print("Please enter a password of atleat 10 characters")
        return False
    elif(password in passwords):
        print("Password matches with last three password")
        print("Please enter a new password")
        return False
    uppercase=0
    lowercase=0
    digit=0
    special_chr=0
    for i in range(len(password)):
        if(password[i].isupper()):
            uppercase+=1
        elif(password[i].islower()):
            lowercase+=1
        elif(password[i].isdigit()):
            digit+=1
        else:
            special_chr+=1
    if(lowercase<2):
        print("Password must contain atleast 2 lowercase character")
        return False
    elif(uppercase<2):
        print("Password must contain atleast 2 uppercase characters")
        return False
    elif(digit<2):
        print("Password must contain atleast 2 digits")
        return False 
    elif(special_chr<2):
        print("Password must contain atrleast 2 special characters")
        return False 
    consecutive_3=three_consecutive_character(password,name) 
    if(consecutive_3==False):
        print("Password should not contain 3 consecutive characters of username")
        return False
    repeated_chr=same_chr_repeated_more_than_3_times(password)
    if(repeated_chr==False):
        print("Password should not contain 3 consecutive same characters")
        return False
    else:
        return True  
while(flag!=True):
    password=input("Enter Password : ")
    flag=validate_password(password,username,last_three_passwords)
print("Your Password is valid\n Thanks")
