#5. Write a Python function that takes two lists and returns True if they have at least one common member.
lst_1 = []
lst_2 = []

print("For list Number 1:")
n = int(input("Enter number of elements : "))
for i in range(0, n): 
    ele = int(input()) 
  
    lst_1.append(ele)  
      
print(lst_1) 


print("For list Number 2:")
n = int(input("Enter number of elements : "))
for i in range(0, n): 
    ele = int(input()) 
  
    lst_2.append(ele)  
      
print(lst_2) 

a = set(lst_1)
b = set(lst_2)

if (a.intersection(b)):
    print("true")
else:
    print("False")

