#user input
n = int(input("Enter the number : "))

def pattern(n):
      #Logic for half pyramid
      for i in range(0, n):
           for j in range(0, i + 1):
                print("* ", end=" ")
           print(" ")
    #logic for inverted half pyramid
      for i in range(n, 0 , -1):
          for j in range(0, i - 1):
               print("* ", end=" ")
          print(" ")
 
pattern(n)