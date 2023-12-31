# -*- coding: utf-8 -*-
"""lab6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mwxk5sKmkB0P8cSp7ymvtZB_8XMgg-Yh
"""

def factorial(intx):
    if intx == 0:
        return 1
    return intx * factorial(intx - 1)


print(factorial(5))


def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)


print(fibb(15))
import numpy as np
arrayx = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

def fprint(arr,idx=0):
  if idx >= len(arr):
    print()
    return
  print(arr[idx],end=' ')
  fprint(arr,idx+1)

fprint(arrayx)

def powerN(a, b):
    if b == 0:
        return 1
    return a * powerN(a, b - 1)


print(powerN(3, 3))

def d_to_b (n ) :
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return d_to_b (n // 2) + str(n % 2)

print(d_to_b(10))

class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

head = Node(arr[0], None)
c_node = head
for var in range(1, len(arr)):
    c_node.next = Node(arr[var])
    c_node = c_node.next


def add(head):
    if head == None:
        return 0
    return head.elem + add(head.next)


print(add(head))

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

head = Node(arr[0], None)
c_node = head
for var in range(1, len(arr)):
    c_node.next = Node(arr[var])
    c_node = c_node.next

def rev_print(head):
    if head == None:
      return
    rev_print(head.next)
    print(head.elem,end=' ')
rev_print(head)
print()

def hocBuilder(height):
  if height == 0:
      return 0
  elif height == 1:
      return 8
  else:
      return 5 + hocBuilder(height-1)
print(hocBuilder(3))

def pattern1(a):
  if a == 0:
    return
  pattern1(a-1)
  for var in range(1,a+1):
    print(var,end=' ')
  print()
pattern1(5)

def pattern2(a,b):
  if a == 0:
    return
  pattern2(a-1,b)
  for var in range(b-a):
    print(' ',end='')
  for var in range(1,a+1):
    print(var,end='')
  print()
pattern2(5,5)

import sys
sys.setrecursionlimit(10000)

class FinalQ:
  def calcProfit(self,x):
    if 25000 == x :
      print('Investment: 25000; Profit: 0.0')
    elif 25000 < x <= 100000:
      p = (4.5/100)*x
      print(f'Investment: {x}; Profit: {p}')
    elif 100000 < x :
      p = (4.5/100)*75000
      p = p + (8/100)*(x-100000)
      print(f'Investment: {x}; Profit: {p}')



  def printx(self,array,idx):
    if(idx<len(array)):
      profit = self.calcProfit(array[idx])
    if idx >= len(array):
      return

    else:
      printx(array,idx+1)





array=[25000,100000,250000,350000]
f = FinalQ()
f.printx(array,0)

class Node:
  def __init__(self, next, bottom, val):
    self.next = next # for next item
    self.bottom = bottom # for nested item check
    self.val = val # The integer value.

my_node = None
if type(arr[0]) != list :
  my_node = Node(None,None,arr[0])
else:
  my_node = Node(None,Node(None,None,None))
def flattenList(arr,node):
  a = []
  for var in range(1,len(arr)):
    if type(arr[var]) != list :
      node.next = arr[var]
    else:
      flattenList(arr[var],node)





output_list = flattenList([1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]],my_node)
