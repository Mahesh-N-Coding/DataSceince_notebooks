#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# * 
# 'hello' }
# -87.8   } values
# 
# - } operators
# / }
# 
# 
# 6 } -values
# 
# 

# 2. What is the difference between string and variable?
# 
# Variable is a name that can refer to any value and String is a value representing text

# 3. Describe three different data types.
# 
# --Lists, Tuples, Dictionary, Sets, Frozenset
# 
# List - 
# 
# 1. List are mutable
# 2. List can have Heterogeneous elements
# 3. List are ordered
# 4. That can contain duplicate values
# 5. Can have nested Lists
# 
# Tuples - 
# 
# 1. Tuples are immutable
# 2. Tuples can have Heterogeneous elements
# 3. Tuples are ordered
# 4. Tuples can contain duplicate values
# 5. Can have nested Tuples
# 
# Dictionary - 
# 
# 1. Dict are Mutable and Nested as List 
# 
# Set --
# 
#  1. Sets are Unordered.
#  2. Only allow unique values
#  
# Frozenset --
# 
# 1. It is just a set but can not modify it after once created.
# 2. So it's used as key's in Dict or as another set 
# 

# In[6]:


#List
List =[2,'Mahesh',4,'Shiva',True]
print(List)
List.append(100)
print(List)

List[1]='Rajesh'
print(List)

List[2]='Rajesh'
print(List)


# In[63]:


#Tuple

Tp=(2,'Shiva','Deepak',True)
print(Tp)

Tp=(3,5,'Rajesh','Rajesh')
print(Tp)

print(Tp[1])

Tp.append(10) # immutable , can not edit
print(Tp)
Tp[1]=10


# In[21]:


#Dictionary

Dict={'A':'Mahesh', "AB":'Shiva', "C":'Deepak'}
print(Dict)

print(Dict['A'])

Dict['A']='Anita'
print(Dict)


# In[59]:


#Sets

Set={1,2,'Mahesh','Chitra','Good'}
print(Set)

Set={1,2,1,'Mahesh'} # Can not have duplicate elements
print(Set)

Set.add(100000)
print(Set)

Set.remove(100000)
print(Set)

#Set[1]=4 #It is unordered so item assignment does not support


# In[57]:


#Frozenset

#It is immutable set once created

Frozen =frozenset({3,6,'Mahesh','Chitra'})
print(Frozen)
Frozen=frozenset({3,10,'Mahesh','Chitra'})
print(Frozen)

Frozen.add(1) # Can not edit it - immutable
print(Frozen[1]) # Unordered, so can not indexed


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')

A combination of operands and operators is called an expression

Expression represents the value

ex: x= 5*2+a --expression 


# In[ ]:


get_ipython().set_next_input('5. This assignment statements, like spam = 10. What is the difference between an expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')

spam =10 --> 10 is the expression and spam=10 is the statement.


# In[66]:


# 6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1


# In[75]:


#7. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3


# In[ ]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')

Variable name should not start with any number so 100 is invalid


# In[ ]:


get_ipython().set_next_input('9. What three functions can be used to get the integer, floating-point number, or string version of a value');get_ipython().run_line_magic('pinfo', 'value')

int(),float(),str()


# In[77]:


#10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + '99' + ' burritos.'


# In[ ]:




