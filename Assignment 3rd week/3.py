#3. Write a Python program to get the largest number from a list.

lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele)  
      
print(lst) 

lst.sort()
print(lst[-1])


