#!/usr/bin/env python
# coding: utf-8

# In[12]:


sayilar=[54,12,15,78,6,45,19,29,8,41,21,26,36,99]
sayac=0
for sayi in sayilar:
   if sayi%3==0:
      print(str(sayi)+(", 3'e kalansız bölünür."))
      sayac=sayac+1
else:
   print("Döngü bitti.")
print("3'e kalansız bölünen sayi adedi "+str(sayac))


# In[ ]:




