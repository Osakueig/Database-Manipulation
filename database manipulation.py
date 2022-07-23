#!/usr/bin/env python
# coding: utf-8

# In[29]:


import sqlite3


# In[14]:


conn = sqlite3.connect("DSdatabase.db")


# In[30]:


connobj = sqlite3.connect('product.db')


# In[31]:


cursor = connobj.cursor()


# In[32]:


cursor.execute("CREATE TABLE product(product_id INT primary key,product_name VARCHAR(50) NOT NULL, price INT)")
connobj.commit()


# In[34]:


entities = (101, 'Desktop computer', 1500)
cursor.execute("INSERT INTO product(product_id ,product_name, price) VALUES(?,?,?)",entities)
connobj.commit()


# In[36]:


cursor.execute("SELECT * FROM product")
rows = cursor.fetchall()

for row in rows:
  print(row)


# In[39]:


product_id = int(input("Enter  product_id: "))
product_name = input("Enter product_name: ")
price = int(input("Enter price: "))
entities = (product_id ,product_name, price)
cursor.execute("INSERT INTO product(product_id ,product_name, price) VALUES(?,?,?)",entities)
connobj.commit()


# In[42]:


cursor.execute("SELECT * FROM product")
rows = cursor.fetchall()

for row in rows:
  print(row)


# In[55]:


# To automatmate data entry


# In[45]:


counter = True
while counter:
    product_id = int(input("Enter  product_id: "))
    product_name = input("Enter product_name: ")
    price = int(input("Enter your price: "))
    entities = (product_id ,product_name, price)
    cursor.execute("INSERT INTO product(product_id ,product_name, price) VALUES(?,?,?)",entities)
    connobj.commit()
    print('Data has been entered !!!')
    print('Do you wish to continue?')
    value = int(input("Press 1 to continue and 0 to quit"))
    if value == 1:
        pass
    elif value == 0:
        print('Merci!!')
        counter = False
    else:
        break


# In[46]:


cursor.execute("SELECT * FROM product")
data = cursor.fetchall()

for d in data:
  print(d)


# In[47]:


products = []


# In[48]:


for d in data:
    products.append({'product_id':d[0], 'product_name':d[1], 'price':d[2]})


# In[53]:


import pandas as pd


dataset = pd.DataFrame(products)
dataset


# In[54]:


dataset.shape


# In[ ]:




