#!/usr/bin/env python
# coding: utf-8

# In[1]:


#opening file 
file=open("C:/Users/DELL/Desktop/hmm.txt","r")
a=file.read()
print(a)


# In[2]:


#In the given file we have a category "X-DSPAM-Confidence" we need to add the values without using sum() function 

file=open("C:/Users/DELL/Desktop/hmm.txt","r")
a=file.readlines()
c=[]
for i in a:
    if "X-DSPAM-Confidence" in i:
        c.append(i)


# In[3]:


c


# In[4]:


#Finding average of the list
a1=0
for i in c:
    a1+=float(i[20:])
print(a1/len(c))


# In[43]:


#The same code displayed above
file=open("C:/Users/DELL/Desktop/hmm.txt","r")
a=file.readlines()
c=[]
d=0
for i in a:
    if "X-DSPAM-Confidence" in i:
        c.append(i)
for j in c:
    d+=float(j[20:])
    
print(d/len(c))
        


# In[ ]:




