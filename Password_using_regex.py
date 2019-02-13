# Python program to validate Password using regex.


import re


def main():
    password = input('Enter Password: ')
    reg = "^(?=.*[az)(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@!#%*?&]{6,20}$"
    # compiling regex
    pat = re.compile(reg)
    # searching  regex
    mat = re.search(pat,password)   
    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("password invalid !!") 


# Driver code
if __name__ == '__main__':
    main()           