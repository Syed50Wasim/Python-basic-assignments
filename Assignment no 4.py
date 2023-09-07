#!/usr/bin/env python
# coding: utf-8
1.What exactly is []?
Ans:-[] represents the absence of elements in a list, and you can use it as a starting point to build a list with one or more elements as needed in your code.2. In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)
Ans:-
# In[2]:


spam = ['a', 'b', 'c', 'd'] 
spam[2] = 'hello' 
print(spam)  

3.What is the value of spam[int(int('3'* 2) / 11)]?
Ans:-
# In[5]:


int('3'*2)


# In[6]:


int(33/11)


# In[7]:


spam[int(int('3'*2)/11)]

4. What is the value of spam[-1]?
Ans:-
The value of spam[-1] in Python corresponds to the last element of the list spam.
# In[9]:


spam[-1]

5. What is the value of spam[:2]?
Let pretend bacon has the list [3.14,'cat',11,'cat',True] for the next three questions.
Ans:-
The value of spam[:2] is a list containing the first two elements of the list spam.
# In[11]:


spam[:2]


# In[13]:


bacon = [3.14, 'cat', 11, 'cat',True]
bacon[:2] 

6.What is the value of bacon.index('cat')?
Ans:-
# In[15]:


bacon.index('cat')

7.How does bacon.append(99) change the look of the list value in bacon?
Ans:-
# In[16]:


bacon = [3.14, 'cat', 11, 'cat',True]
bacon.append(99)


# In[17]:


bacon

8.How does bacon.remove('cat') change the look of the list in bacon?
Ans:-
# In[19]:


bacon = [3.14, 'cat', 11, 'cat', True, 99]


# In[20]:


bacon.remove('cat') 


# In[21]:


bacon

9.What are the list concatenation and list replication operators?
Ans:-
In Python, you can concatenate lists using the + operator, and you can replicate (duplicate) a list using the * operator.

# In[23]:


#CONCATINATION
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2 
print(result)  


# In[24]:


#REPLICATE 
original_list = [1, 2, 3]
replicated_list = original_list * 3 
print(replicated_list) 

10. What is difference between the list methods append() and insert()?
Ans:-
The append() and insert() methods in Python are both used to add elements to a list, but they differ in how they add elements and where they place them in the list
# In[27]:


#Append meathod
my_list = [1, 2, 3]
my_list.append(4)


# In[26]:


my_list


# In[28]:


#insert meathod 
my_list = [1, 2, 3]
my_list.insert(1, 4)  


# In[29]:


my_list

11. What are the two methods for removing items from a list?
Ans:-
The remove() method is used to remove the first occurrence of a specified element from the list. It takes one argument, which is the element you want to remove.
The pop() method is used to remove an element from the list at a specific index and return that element
# In[30]:


#remove meathod 
my_list = [1, 2, 3, 2, 4]
my_list.remove(2) 


# In[31]:


my_list


# In[33]:


#pop() meathod
my_list = [1, 2, 3, 4]
removed_element = my_list.pop(2)  


# In[34]:


removed_element 

12.Describe how list values and string values are identical.
Ans:-
List values and string values are both types of data structures in programming, but they have different purposes and characteristics. However, there are some similarities and ways in which they can be considered identical.
while lists and strings share some similarities due to their sequential nature and the ability to access elements through indexing, they have distinct characteristics and use cases. Lists are versatile collections for various data types, while strings are specifically designed for text manipulation and are immutable.13. Whats the difference between tuples and lists?
Ans:-

Tuples and lists are both data structures in programming, but they have several key differences
MUTABILITY:-
Lists: Lists are mutable, which means you can change their contents after they are created. You can add, remove, or modify elements within a list.
Tuples: Tuples are immutable, which means once you create a tuple, you cannot change its contents. You cannot add, remove, or modify elements within a tuple. If you need to make changes, you must create a new tuple.

SYNTAX:-
Lists: Lists are defined using square brackets []. For example: my_list = [1, 2, 3].
Tuples: Tuples are defined using parentheses (). For example: my_tuple = (1, 2, 3).

choose between lists and tuples based on whether you need mutable or immutable collections, respectively, for your specific use case. Lists are flexible for dynamic data, while tuples are suitable for situations where data should remain constant.


14. How do you type a tuple value that only contains the integer 42?
Ans:-
To create a tuple that contains only the integer 42, you can simply enclose the integer in parentheses.

# In[1]:


my_tuple = (42,)


# In[2]:


my_tuple

',' after the integer 42. This comma is necessary to indicate that you are creating a tuple with a single element. Without the comma, Python would interpret the parentheses as an expression grouping, and you would end up with an integer rather than a tuple15. How do you get a list values tuple form? How do you get a tuple values list form?
Ans:-
To convert a list to a tuple or a tuple to a list in Python, you can use built-in functions like tuple() and list().
# In[3]:


my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)


# In[4]:


type(my_tuple)


# In[5]:


my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)


# In[6]:


type(my_list)

16.Variables that contain list values are not necessarily lists themselves. Instead, what do they
contain?
Ans:-
Variables that "contain" list values in Python actually store references or pointers to those lists in memory. In other words, they hold the memory address where the list data is stored, rather than the actual list data itself. This concept is important to understand because it affects how variables and lists behave when assigned to new variables or passed as arguments to functions17. How do you distinguish between copy.copy() and copy.deepcopy()?
Ans:-
copy.copy() and copy.deepcopy() are two functions provided by the Python copy module, and they are used to create copies of objects, especially complex data structures like lists and dictionaries. However, they behave differently in terms of copying nested objects and references.
# In[ ]:




