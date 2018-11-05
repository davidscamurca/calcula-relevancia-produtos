
# coding: utf-8

# In[2]:


import pandas as pd


# In[6]:


df = pd.read_csv("./produto_vendas_visitas.txt", sep=';', names=["id_product","qtd_sales","qtd_visits"])


# In[8]:


df = df.groupby("id_product", as_index=False).agg({"qtd_sales":"sum","qtd_visits":"sum"})


# In[21]:


def calc_score_sales(row):
    # 2 * qtd_sales + qtd_visits
    return 2 * row[1] + row[2]


# In[22]:


df["score"] = df.apply(calc_score_sales, axis=1)


# In[27]:


df = df[["id_product","score"]].copy()


# In[30]:


df.sort_values(["score"], inplace=True, ascending=False)


# In[33]:


df.to_csv("./saida_product_rev_2018", index=False)

