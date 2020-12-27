#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd

path = r'한국언론진흥재단_뉴스빅데이터_메타데이터_코로나_20200831.csv'
raw_data = pd.read_csv(path, encoding='CP949',engine="python", sep=',')
df = pd.DataFrame(raw_data)
df['통합 분류1']


# In[38]:


raw_category_list = list(df['통합 분류1'])
raw_category_list


# In[39]:


category = []
for raw_category in raw_category_list :
    temp = str(raw_category).split('>')
    category.append(temp[0])
category


# In[40]:


# 중복되는 카테고리 제거
category_set = list(set(category))
category_set


# In[41]:


# y 데이터 숫자로 변경
for i in range(len(category)) :
    for j in range(len(category_set)) :
        if category[i] == category_set[j] :
            category[i] = j
y = category
y


# In[45]:


txt_list = list(df['키워드'])
new_txt = list()
new_txt_list = list()
for txt in txt_list :
    new_txt = str(txt).split(',')
    new_txt_list.append(new_txt)


# In[ ]:


for txt in new_txt_list :
    for key in txt :
        if 

