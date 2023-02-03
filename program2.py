my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

y=[]
#2 refers the step size in the range function
for i in range(0,len(my_list),2):
    y.append(my_list[i])

print(y)
