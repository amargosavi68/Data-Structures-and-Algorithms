'''
@author: Amar Gosavi
Implementation of stack using linked list
'''

class Node():
     def __init__(self, data=None):
          self.data = data
          self.next = None
     

class Stack():
     def __init__(self):
          self.top = None
     
     def push(self, data):
          node = Node(data)
          if self.top == None:
               self.top = node
          else:
               node.next = self.top
               self.top = node

     def pop(self):
          if self.top == None:
               print("No node is present in stack")
          else:
               self.top = self.top.next
     
     def print_stack(self):
          temp = self.top
          while temp:
               print(temp.data, end=" -> ")
               temp = temp.next
          print("None")
     

def main():
     print("\t******** Stack **********")
     print("1. Push")
     print("2. Pop")
     print("3. Display")
     print("4. Quit")

     stack_obj = Stack()

     ch = int(input("Enter your choice: "))

     while ch > 0 and ch < 4:
          if ch == 1:
               data = int(input("Enter the value: "))
               stack_obj.push(data)
          elif ch == 2:
               stack_obj.pop()
          else:
               stack_obj.print_stack()

          ch = int(input("Enter your choice: "))

if __name__ == "__main__":
     main()