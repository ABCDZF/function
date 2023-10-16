#!/usr/bin/env python
# coding: utf-8

# In[11]:


#1
#The keyword used to create a function is "def".
def odd():
    for i in range(1,26,2):
        print(i)
odd()


# In[9]:


#2
*args and kwargs are used to pass a variable number of arguments to a function.

*args = The *args syntax allows a function to accept a variable number of positional arguments

**kwargs = **kwargs syntax allows a function to accept a variable number of keyword arguments.



# In[10]:


# Example using *args
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15
     


# In[12]:


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="chandan", age=21, country="INDIA")


# In[13]:


#3
Ans: An iterator in Python is an object that implements the iteration. It provides a way to access the elements of a collection sequentially without exposing the underlying implementation details

[] = The iter() method is used to initialize the iterator object and the next() method is used for iteration.



# In[22]:


my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
iterator = iter(my_list)
for i in range(5):
    print(next(iterator))


# In[23]:


#4
Ans: A generator function in Python is a special type of function that allows you to define an iterator in a more concise and efficient way. It is defined using the def keyword, just like a regular function, but instead of using the "return" statement to return a value, it uses the "yield" keyword.

[] The "yield" keyword is used in a generator function to define a value to be returned each time the iterator is iterated over. When a generator function is called, it returns a generator object, which can be iterated over using a for loop or by explicitly calling the next() function on it.

[]Example = Generator function of Fibonacci Series


# In[24]:


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib_gen = fibonacci_generator()

for i in range(10):
    print(next(fib_gen))
     


# In[25]:


#5
def prime_generator():
    primes = []
    num = 2
    while True:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
            yield num
        num += 1
prime_gen = prime_generator()

for _ in range(20):
    print(next(prime_gen))
     


# In[26]:


#6
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# In[29]:


#7
string = 'pwskills'
result = [char for char in string]
print(result)
     


# In[30]:


#8

def is_palindrome(number):
    original_number = number
    reverse_number = 0

    while number > 0:
        remainder = number % 10
        reverse_number = (reverse_number * 10) + remainder
        number = number // 10
        if original_number == reverse_number:
            return True
        else:
            return False
     


# In[ ]:


num = int(input("Enter a number: "))
if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")


# In[31]:


#9
odd_Num_list = [element for element in range(1, 101) if element % 2 == 1 ]
print(odd_Num_list)


# In[ ]:




