# -*- coding: utf-8 -*-
"""lab5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19Mxh5PGBf4BdQ1Qp0zHBfpwyoYIxT0D2
"""

# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

"""Implement the Stack class first

Take help from this [stack note](https://docs.google.com/document/d/1SAdvXigDtA5tIkk7Fs1wGs9-hEROYUBOY1v6VxBpU60/edit?usp=sharing)
"""

class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next

class Stack:
  def __init__(self):
    self.__top = Node()

  def push(self,elem):
    #TO DO
    new_node = Node(elem,self.__top)
    self.__top = new_node

  def pop(self):
    #TO DO
    if self.__top.elem == None:
      return
    else:
      temp = self.__top.elem
      self.__top = self.__top.next
      return temp


  def peek(self):
    #TO DO
    return self.__top.elem

  def isEmpty(self):
    #TO DO
    if self.__top.elem == None and self.__top.next == None:
      return True
    return False

st = Stack()
st.push(4)
st.push(3)
st.push(5)
st.push(1)
st.push(9)


print('Peeked Element: ',st.peek()) #This should print 9
print('Popped Element: ',st.pop()) #This should print 9
print('Popped Element: ',st.pop()) #This should print 1
print('Popped Element: ',st.pop()) #This should print 5
print('Peeked Element: ',st.peek()) #This should print 3
print('Popped Element: ',st.pop()) #This should print 3
print('Popped Element: ',st.pop()) #This should print 4
print('Peeked Element: ',st.peek()) #This should print None
print('Popped Element: ',st.pop()) #This should print None
print(st.isEmpty()) #This should print True

"""You can print your stack using this code segment"""

def print_stack(st):
  if st.isEmpty():
    return
  p = st.pop()
  print('|',p,end=' ')
  if p<10:
    print(' |')
  else:
    print('|')
  #print('------')
  print_stack(st)
  st.push(p)

st = Stack()
st.push(4)
st.push(3)
st.push(5)
st.push(1)
st.push(9)
print_stack(st)
print('------')

"""Task 1: Parenthesis Balancing:"""

def balance_parenthesis(string):
  #TO DO
  my_stack = Stack()
  for var in range(len(string)):
    if string[var] == '[' or string[var] == '{' or string[var] == '(':
      my_stack.push(string[var])




    if string[var] == ')' or string[var] == '}' or string[var] == ']':
      if (string[var] == ')' and my_stack.peek() == '('):
        my_stack.pop()
      elif (string[var] == '}' and my_stack.peek() == '{'):
        my_stack.pop()
      elif (string[var] == ']' and my_stack.peek() == '['):
        my_stack.pop()
      else:
        return False
    else:
      continue




  if my_stack.isEmpty():
    return True
  else:
    return False


print('Test 01')
s = '1+2*(3/4)'
returned_value = balance_parenthesis(s)
print('Balanced') if returned_value else print('Unbalanced') #This should print Balanced
unittest.output_test(returned_value, True)
print('-----------------------------------------')

print('Test 02')
s = '1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14' #mismatch
returned_value = balance_parenthesis(s)
print('Balanced') if returned_value else print('Unbalanced') #This should print Unbalanced
unittest.output_test(returned_value, False)
print('-----------------------------------------')

print('Test 03')
s = '[10*[3-(5-2)]' #unpaired opening bracket
returned_value = balance_parenthesis(s)
print('Balanced') if returned_value else print('Unbalanced') #This should print Unbalanced
unittest.output_test(returned_value, False)
print('-----------------------------------------')

print('Test 04')
s = '(A+B)-C)' #unpaired closing bracket
returned_value = balance_parenthesis(s)
print('Balanced') if returned_value else print('Unbalanced') #This should print Unbalanced
unittest.output_test(returned_value, False)
print('-----------------------------------------')

print('Test 05')
s = '([A+B]-C)/{D*E}+[2*[(2A+5){5B}]-{7C-9AB}]'
returned_value = balance_parenthesis(s)
print('Balanced') if returned_value else print('Unbalanced') #This should print Balanced
unittest.output_test(returned_value, True)
print('-----------------------------------------')

"""Task 2: Diamond Count"""

def diamond_count(stack,string):
  #TO DO
  my_stack = stack
  c = 0
  for var in range(len(string)):
    if string[var] == '<':
      my_stack.push(string[var])
    if string[var] == '>':
      if my_stack.isEmpty():
        continue
      else:
        my_stack.pop()
        c+=1
  return c






print('Test 01')
stack = Stack()
string = '<..><.<..>> '
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')


print('Test 02')
stack = Stack()
string = '<<<..<......<<<<....>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 1
unittest.output_test(returned_value, 1)
print('-----------------------------------------')


print('Test 03')
stack = Stack()
string = '>>><...<<..>>...>...>>>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')

"""BONUS (Tower of God)"""

def remove_block(st, n):
  #TO DO
  pass



print('Test 01')
st = Stack()
st.push(4)
st.push(19)
st.push(23)
st.push(17)
st.push(5)
print('Stack:')
print_stack(st)
print('------')
remove_block(st,2)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()

print('Test 02')
st = Stack()
st.push(73)
st.push(85)
st.push(15)
st.push(41)
print('Stack:')
print_stack(st)
print('------')
remove_block(st,3)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()

