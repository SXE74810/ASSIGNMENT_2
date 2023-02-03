def unique(x):#function definition
   myset = set(x)#Convert the list to set to eliminate the duplicate elements
   for i in range(0,len(x)):
       myset.add(x[i])#append the elements to a new set
       return myset

number_of_elements = int(input("enter the number of elements : "))

list1 = []

for i in range(0,number_of_elements):
    list1.append(int(input("enter the elements : ")))#user entered elements are added in to the new list

y =unique(list1)#unique function call
print(list(y)) #convert the set to list for the final output