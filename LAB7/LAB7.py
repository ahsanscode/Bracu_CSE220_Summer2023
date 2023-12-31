# -*- coding: utf-8 -*-
"""LAB7

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PlULcNlVM9LyEBec6LCDENGbeGZtmMxK
"""

# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

"""Run this cell first"""

class Node:
  def __init__(self, elem, next = None):
    self.elem, self.next = elem, next

def create_linked_list(arr):
  head = Node(arr[0])
  tail = head
  for i in arr[1:]:
    new_node = Node(i)
    tail.next = new_node
    tail = new_node
  return head

def count(head):
  count = 0
  while head != None:
    count += 1
    head = head.next
  return count

def print_linked_list(head):
  while head != None:
    print(head.elem, end = '-> ')
    head = head.next
  print('None')
  print()

"""#TASK 1
> You can use Dictionary, Set and membership operator (in/not in) only for this task. Membership Operator takes constant time in these unordered collections. See this [link](https://stackoverflow.com/questions/13884177/complexity-of-in-operator-in-python) for details.



However,


>  ***DO NOT USE*** Membership Operator in List, String for this task.

> You can traverse the array ***ONLY ONCE*** (i.e. no nested loop).




"""

#Do by yourself
def nerdy_run(path,k):
  try:
    for var in range(len(path)):
      c_elem = path[var]
      for varx in range(var+1,var+k ):
        if  path[varx] == c_elem:
          return c_elem
  except:
    return None
  return None

def main():

  path = [6,7,8,9,5,9]
  k = 3
  result = nerdy_run(path,k)
  unittest.output_test(result, 9)
  print(f'Duplicate value within range {k} is: {result}') #Duplicate value within range 3 is: 9

  print('===================================')
  path = [6,7,8,9,5,6]
  k = 4
  result = nerdy_run(path,k)
  unittest.output_test(result, None)
  print(f'Duplicate value within range {k} is: {result}') #Duplicate value within range 4 is: None

  print('===================================')
  path = [0.21,1.21,4.67,0.21,0.45,1.9]
  k = 7
  result = nerdy_run(path,k)
  unittest.output_test(result, 0.21)
  print(f'Duplicate value within range {k} is: {result}') #Duplicate value within range 7 is: 0.21


if __name__ == "__main__":
  main()

"""#TASK 2
Complete the following methods:

>  __hash_function()

> search_hashtable()




"""

class Hashtable:
  def __init__(self, size):
    self.ht = [None]*size


  def insert(self, s):
    if self.search_hashtable(s) == 'Found':
      print(s,'Already Inserted. Cannot reinsert.')
      print('===============================')
      return
    key = self.__hash_function(s)
    node = Node(s)
    if self.ht[key] == None:
      self.ht[key] = node
    else:
      node.next = self.ht[key]
      self.ht[key] = node

  def create_from_array(self, arr):
    for i in arr:
      self.insert(i)

  def print_hashtable(self):
    idx = 0
    for i in self.ht:
      print(idx, ':', end = ' ')
      print_linked_list(i)
      idx += 1


  #Do by yourself



  def __hash_function(self, s):
    if len(s) % 2 == 1:
      s += 'N'
    summation = 0
    for i in range(0,len(s), 2):
      summation += int( str(ord(s[i]) ) + str( ord(s[i+1]) ))
    return summation % len(self.ht)

  def search_hashtable(self, s):
    key = self.__hash_function(s)
    node = self.ht[key]
    while node != None:
      if node.elem == s:
        return 'Found'
      node = node.next

    return 'Not Found'

arr = ['Colt', 'Cordelius', 'Shelly', 'Doug', 'Emz', 'Bo']
ht = Hashtable(5)
ht.create_from_array(arr)
ht.print_hashtable()
'''
0 : None

1 : Bo-> None

2 : Emz-> Colt-> None

3 : Shelly-> None

4 : Doug-> Cordelius-> None

'''

print('======================')
result = ht.search_hashtable('Doug')
unittest.output_test(result, 'Found')
print(f'Doug {result}') #This should print 'Doug Found'

print('======================')
ht.insert('Doug') #This will print 'Doug Already Inserted. Cannot reinsert.'
ht.print_hashtable()
'''
0 : None

1 : Bo-> None

2 : Emz-> Colt-> None

3 : Shelly-> None

4 : Doug-> Cordelius-> None

'''

print('======================')
result = ht.search_hashtable('Edgar')
unittest.output_test(result, 'Not Found')
print(f'Edgar {result}') #This should print 'Edgar Not Found'

print('======================')
ht.insert('Edgar')
ht.print_hashtable()
'''
0 : Edgar-> None

1 : Bo-> None

2 : Emz-> Colt-> None

3 : Shelly-> None

4 : Doug-> Cordelius-> None

'''

print('======================')
result = ht.search_hashtable('Edgar')
unittest.output_test(result, 'Found')
print(f'Edgar {result}') #This should print 'Edgar Found'

"""#TASK 3
Complete the following methods:



> create_layered_hashtable()

> search_element()
"""

class Layered_Hashtable:
  def __init__(self, express_array_size):
    self.express_array = [None] * express_array_size

  def print_express_lane(self):
    for i in self.express_array:
      print(i.elem, end = ' '*10)
    print()

  def print_layered_hashtable(self):
    print('Express Lane is:')
    self.print_express_lane()

    for i in range (len(self.express_array)-1):
      node = self.express_array[i]
      next_node = self.express_array[i+1]
      print(f'Normal Lane Nodes between Express Lane Node {node.elem} and Express Lane Node {next_node.elem} are: ')
      while node != next_node:
        print(node.elem, end = '->')
        node = node.next
      print()

    print(f'Normal Lane Nodes ending in the Express Lane Node: {node.elem}')

  #DO IT YOURSELF
  def create_layered_hashtable(self, linked_list_head):
    a = len(self.express_array)
    b = 1
    temp = linked_list_head
    while temp.next != None:
      b+=1
      temp = temp.next
    c = (b//a)+1


    temp = linked_list_head
    bucket_idx = 0
    for var in range(b):
      if var % c == 0:
        self.express_array[bucket_idx] = temp
        bucket_idx+=1
        temp = temp.next
        continue
      temp = temp.next
    return self.express_array


#DO IT YOURSELF


  def search_element(self,k):
    arr = self.express_array
    a = len(self.express_array)
    t = arr[0]

    if t.elem == k:
      return 'Found'


    idx = 0

    for var in range(1,a):
      if arr[var].elem == k:
        return 'Found'
      elif arr[var].elem > k  :
        break
      t = arr[var]
      idx = var
    # print(t.elem)
    try:
      while t.next != arr[idx+1]:
        if t.elem == k:
          return 'Found'
        t = t.next
    except:
      while t.next != None:
        if t.elem == k:
          return 'Found'
        t = t.next
    if t.elem == k:
      return 'Found'
    elif k > t.elem:
      return 'Not Found'
    else:
      return 'Not Found'

arr = [4,6,9,18,25,37,62,67,79,84]
head = create_linked_list(arr)
express_array_size = 4

layered_ht = Layered_Hashtable(express_array_size)
layered_ht.create_layered_hashtable(head)
layered_ht.print_layered_hashtable()

print('==========1===========')
result = layered_ht.search_element(67)
unittest.output_test(result, 'Found')
print(f'67 {result}') #67 Found

print('==========2===========')
result = layered_ht.search_element(84)
unittest.output_test(result, 'Found')
print(f'84 {result}') #84 Found

print('==========3===========')
result = layered_ht.search_element(1)
unittest.output_test(result, 'Not Found')
print(f'1 {result}') #1 Not Found

print('==========4===========')
result = layered_ht.search_element(92)
unittest.output_test(result, 'Not Found')
print(f'92 {result}') #92 Not Found

print('==========5===========')
result = layered_ht.search_element(41)
unittest.output_test(result, 'Not Found')
print(f'41 {result}') #41 Not Found

