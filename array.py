'''
@author: Amar Gosavi
Implementation of array
'''

N = int(input("Enter the number of elements in array"))
arr = []
for i in range(N):
     temp = int(input(f"Enter {i+1} element: "))
     arr.append(temp)

for num in arr:
     print(num, end=" ")
