#!/usr/bin/env python
# coding: utf-8

# In[1]:


for prime in range(2, 102):
    is_prime = True  
    for number in range(2, prime):
        if prime % number == 0:
            is_prime = False  
            break
    if is_prime:
        print(prime, "is a prime number")


# In[ ]:




