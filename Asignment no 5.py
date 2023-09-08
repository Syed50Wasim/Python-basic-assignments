#!/usr/bin/env python
# coding: utf-8
1. What does an empty dictionary's code look like?
Ans:-
In Python, an empty dictionary is represented using curly braces {} with no key-value pairs inside.
# In[1]:


empty_dict = {}


# In[2]:


empty_dict = dict()

Both of these methods will create an empty dictionary that you can later populate with key-value pairs as needed.2.What is the value of a dictionary value with the key 'foo' and the value 42?
Ans:-
Dictionaries consist of key-value pairs, where each key is associated with a specific value. In this case, the key 'foo' is associated with the value 42. You can access the value associated with the key 'foo' by using the key as an index in square bracets.
# In[3]:


my_dict = {'foo': 42}
value = my_dict['foo']
print(value) 

3. What is the most significant distinction between a dictionary and a list?
Ans:-

The most significant distinction between a dictionary and a list is how they store and retrieve data:

Data Structure:
List: A list is an ordered collection of elements where each element is identified by an index, starting from 0. Lists are typically used to store a sequence of values, and the order of elements matters. You access elements in a list by their index.
Dictionary: A dictionary is an unordered collection of key-value pairs. Instead of using numeric indices, dictionaries use unique keys to associate values. Keys must be unique within a dictionary, and they are used to access and retrieve corresponding values.

Data Type:
List: Lists can store elements of any data type, including other lists.
Dictionary: Dictionaries can store values of various data types, but their keys are typically strings, numbers, or other immutable types.

Lists are used to store ordered sequences of elements accessible by index, while dictionaries are used to store key-value pairs, allowing you to associate values with specific keys for efficient retrieval. 4.What happens if you try to access spam ['foo'] if spam is {'bar':10}?
Ans:-
In this case, spam only contains one key-value pair with the key 'bar', and there is no key 'foo' in the dictionary. To avoid a KeyError, you should ensure that the key you are trying to access actually exists in the dictionary or use error handling mechanisms like try and except to handle the exception gracefully.
# In[4]:


spam = { 'bar': 100 }
value = spam['foo'] 

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and
'cat' in spam.keys()?
Ans:-
There is no practical difference between the expressions 'cat' in spam and 'cat' in spam.keys(). Both expressions are used to check if the key 'cat' is present in the dictionary spam, and they will yield the same result.
The in operator, when used with a dictionary, checks for key membership directly in the dictionary, so both 'cat' in spam and 'cat' in spam.keys() will return True if 'cat' is a key in the dictionary spam, and False if it's not6.If a dictionary is stored in spam, what is the difference between the expressions  'cat' in spam and
'cat' in spam.values()?
Ans:-
When you have a dictionary stored in the variable spam, there is a significant difference between the expressions 'cat' in spam and 'cat' in spam.values().
This expression checks if the key 'cat' is present in the keys of the dictionary spam. It returns a Boolean value (True or False) based on whether the key exists in the dictionary.
If 'cat' is a key in spam, it will return True. Otherwise, it will return False.7. What is a shortcut for the following code?
if  'color' not in spam:
spam['color'] = 'black'
Ans:-
The setdefault() method to achieve the same result with a shorter code.
# In[5]:


spam.setdefault('color', 'black')

8.How do you "pretty print" dictionary values using which module and function?
Ans:-
To "pretty print" dictionary values in Python, you can use the pprint module from the pprint library. The primary function for pretty-printing dictionary values is pprint()
# In[6]:


import pprint

my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
pprint.pprint(my_dict)


# In[7]:


# Create a PrettyPrinter object with custom options
pp = pprint.PrettyPrinter(indent=4, width=20 )
                          
pp.pprint(my_dict)


# In[ ]:




