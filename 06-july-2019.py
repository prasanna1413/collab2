#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function of the list
lst1
print(min(lst1))
print(max(lst1)) Day objectives
Python data structures
Lists
Tuples
Dictionaries
Basic Program sets on data structures
advanced problem set
contact application(dictionary object)
Data structures
To store ,search and Sort the data
pyhton data structures
lists
It is one of the common data structures supports by python,the list items are separated by comma operator and enclosed in square brackets
example:
list1 = [1,6,2,18,9]
list2 = ["gitam",12,12,15.5,"hyderabad"]
print(sum(lst1))
print(sum(lst1)//len(lst1))
print(sum(lst1[1::2])/len(lst1[1::2]))


# In[2]:


# Function of the list
lst1
print(min(lst1))
print(max(lst1))
print(sum(lst1))
print(sum(lst1)//len(lst1))
print(sum(lst1[1::2])/len(lst1[1::2]))


# #  Linear search
# Linear search algorithm can be applied on duplicate and unique list
# Unique list : All items of the list are appeared as only one
# Duplicate list : The items of the list can be appeared more than one
# Linear search algorithm can be applied on sorted list or unsorted list

# In[3]:


# Function to search the data in a list
# Search is found then return the index if not return -1
def linearsearch1(li,taritem):
   for x in range(len(li)):
       if li[x] == taritem:
           return x
       return -1
li = [1,19,6,2,8,18,3]
linearsearch1(li,225)


# In[4]:


# Function
# Input : [1,5,9,6,5,15,1,2,5],key=5 # Duplicate
# Output : 1 4 8
def linearsearch2(li,taritem):
   for x in range(len(li)):
       if li[x] == taritem:
           print(x,end=" ")
   return 

li = [1,5,9,6,5,15,1,2,5]
linearsearch2(li,5)         


# In[5]:


# Function
# i/p : list
#o/p : seq of characters
# Test case
# [1,5,9,6,5,15,1,2,5],tar=5 --!! !!!!! !!!!!!!!!

def linearSearch3(li,tarItem):
   # Implement the logic
   for x in range(len(li)):
       if li[x] == tarItem:
           j=0
           while j!=x+1:
               print("!",end=" ")
               j=j+1
           print(end=" ")
   return
li = [1,5,9,6,5,15,1,2,5]
linearSearch3(li,5)


# In[6]:


# Function
# i/p: List
# o/p: Formatted
# Test case:
# [12,2,45,9,18,15,36] --60
#A list item which is perfectly multiple of 3 and 5

def linearSearch4(li):
   sum=0
   for x in range(len(li)):
       if li[x] %3 ==0 and li[x] % 5==0 :
           sum += li[x] #sum=sum + li[x]
   return sum
li= [12,2,45,9,18,15,36]
linearSearch4(li)


# In[ ]:




