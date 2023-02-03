def count(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():#checking for the number of upper case elements in the string
            upper = upper + 1
        if i.islower():
            lower = lower +  1#checking for the number of lower case elements in the string
    print("No. of Upper-case characters : ",upper, "\nNo. of Lower-case characters : ", lower)



string = input("enter the string : ")
count(string)