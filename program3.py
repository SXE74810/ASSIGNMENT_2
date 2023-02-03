x = [23, "Python", 23.98]

y=[] #new list

for i in range(0, len(x)):
    y.append(type(x[i]))
    #appended the results in to the new list

#type is used to find the data type of a variable
print(y)