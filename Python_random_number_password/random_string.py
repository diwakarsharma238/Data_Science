#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


import string


# 1. Generate 6 digit random secure OTP

# In[3]:


print(random.randint(1,999999))


# 2.Generate random string length 5
# ****String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.

# In[5]:


#Function to generate random string default length is 10 characters.
def random_string(length=5):
    character_lower=''
    character_upper=''
    character_special=''
    
    #character sets of lower case, upper case letters and special symbol
    character_lower=string.ascii_lowercase
    character_upper=string.ascii_uppercase
    character_special=string.punctuation
    
    #selecting 1 lower case, 1 upper case letter and 1 special character
    random_str=random.choice(character_lower)
    random_str+=random.choice(character_upper)
    random_str+=random.choice(character_special)
    
    # rest of the characters (length of password - 3 ( 3 characters already choosen above))
    random_str+=''.join( random.choice(string.ascii_letters) for i in range(length-3))
    
    #shuffling the characters of random password string
    return(''.join(random.sample(random_str,len(random_str))))


my_random_string=random_string()
print(my_random_string)


# 3. Generate a random Password which meets the following condition ** Password must be 10 characters long ** It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

# In[7]:


#Function to generate random password default length is 10 characters. 
def random_password(length=10):
    character_number=''
    character_upper=''
    character_special=''
    
    #character sets of nubers, upper case letters and special symbol
    character_number=string.digits
    character_upper=string.ascii_uppercase
    character_special=string.punctuation
    
    character_all=string.ascii_letters+string.digits+string.punctuation
    
    #selecting 1 number, 2 upper case letter and 1 special character (mandatory req of the random password)
    random_str=random.choice(character_number)
    random_str+=random.choice(character_upper)+random.choice(character_upper)
    random_str+=random.choice(character_special)
    
    # rest of the characters (length of password - 4 ( 4 characters already choosen above))
    random_str+=''.join( random.choice(character_all) for i in range(length-4))
    
    #shuffling the characters of random password string and returning the final random password
    return(''.join(random.sample(random_str,len(random_str))))


my_random_password=random_password()
print(my_random_password)


# In[ ]:




