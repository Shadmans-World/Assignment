#2. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
a = input()

b=a

c=d=0

c = a.find('not')
d = a.find('poor')

if(c>=0 and d>=0):
    b = b.replace(b[c:d+4],'good')
    print(b)

