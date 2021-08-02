'''
@author: Amar Gosavi
Implementation of Linked List
'''

class Node():
     def __init__(self, data=None):
          self.data = data
          self.next = None
     
class LinkedList():
     def __init__(self):
          self.head = None
          self.tail = None
     
     def insert_at_beginning(self, data):
          node = Node(data)
          if self.head == None:
               self.head = node
               self.tail = node
          else:
               node.next = self.head
               self.head = node
     
     def insert_at_end(self, data):
          node = Node(data)
          if self.head == None:
               self.head = node
               self.tail = node
          else:
               self.tail.next = node
               self.tail = node
     
     def insert_at_position(self, index, data):
          prev_node = self.head
          temp = self.head
          if index == 0:
               self.insert_at_beginning(data)
          else:
               for i in range(index):
                    prev_node = temp
                    temp = temp.next
               node = Node(data)
               prev_node.next = node
               node.next = temp

     def delete_from_beginning(self):
          if self.tail == self.head:
               self.head = None
               self.tail = None
          self.head = self.head.next
     
     def delete_from_end(self):
          temp = self.head 
          prev_node = temp
          if self.tail == self.head:
               self.head = None
               self.tail = None
          while temp.next != None:
               prev_node = temp
               temp = temp.next
          prev_node.next = None
          self.tail = prev_node

     def delete_from_position(self, index):
          prev_node = self.head
          temp = self.head
          if index == 0:
               self.delete_from_beginning()
          else:
               for i in range(index):
                    prev_node = temp
                    temp = temp.next
               prev_node.next = temp.next

     def print_list(self):
          temp = self.head
          while temp != None:
               print(temp.data, end=" -> ")
               temp = temp.next
          print("None")


def main():
     print("\t----------- Menu ------------")
     print("1.Insert at Beginning")
     print("2.Insert at end")
     print("3. Insert At Position")
     print("4.Delete from Beginning")
     print("5.Delete from end")
     print("6. Delete from Position")
     print("7. Display")
     print("8. Quit")
     ch = int(input("Please enter your choice: "))
     obj = LinkedList()
     while ch > 0 and ch < 8:
          if ch == 1:
               data = int(input("Enter value:"))
               obj.insert_at_beginning(data)
          elif ch == 2:
               data = int(input("Enter value:"))
               obj.insert_at_end(data)
          elif ch == 3:
               index = int(input("Enter the position where you want insert data:"))
               data = int(input("Enter value:"))
               obj.insert_at_position(index, data)
          elif ch == 4:
               obj.delete_from_beginning()
          elif ch == 5:
               obj.delete_from_end()
          elif ch == 6:
               index = int(input("Enter the position from where you want to delete:"))
               obj.delete_from_position(index)
          else:
               obj.print_list()
          
          ch = int(input("Please enter your choice: "))


if __name__ == "__main__":
     main()