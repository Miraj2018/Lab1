#!/usr/bin/env python
# coding: utf-8

# In[1]:


marks = int(input('Enter your marks:'))
if marks>60 and marks<=100:
    print('GRADE A')
elif marks>=40 and marks<=60:
    print('GRADE B')
elif marks<40 and marks>20:
    print("GRADE C")
elif marks>100:
    print('Enter a value between 1-100')
else:
    print('you are fail')


# In[ ]:




