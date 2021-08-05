'''
@author: Amar Gosavi
Implementation of stack using array
'''
class Stack:
     def __init__(self):
          self.stack = []
          self.length = 0
     
     def push(self, data):
          self.stack.insert(0, data)
          self.length += 1
     
     def pop(self):
          if self.length <= 0:
               print("Stack underflow")
          else:
               self.stack.pop(0)
               self.length -= 1
     
     def display(self):
          for data in self.stack:
               print(data, end=" ")

def main():
     print("\t*****Stack Using Array*******")
     print("1.Push")
     print("2.Pop")
     print("3.Display")
     print("4.Quit")
     ch = int(input("Enter your choice: "))
     stack = Stack()
     while ch > 0 and ch < 3:
          if ch == 1:
               data = int(input("Enter a value"))
               stack.push(data)
          elif ch == 2:
               stack.pop()
          else:
               stack.display()
          ch = int(input("Enter your choice: "))

if __name__ == "__main__":
     main()