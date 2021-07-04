#6. create custom count function.
lst = []
count = 0
n = int(input("Enter number of elements : "))
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele)  
      
print(lst) 

a = int(input("which element you want to count? : "))
for i in range(0, len(lst)):
    if a ==lst[i]:
        count=count+1
print(count)
