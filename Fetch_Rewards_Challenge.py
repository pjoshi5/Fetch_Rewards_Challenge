#!/usr/bin/env python
# coding: utf-8

# # FETCH REWARDS: Data Engineer Coding Challenge

# ### Submitted by -
#     Pradeep Joshi

# ### Problem Statement
#     This challenge will focus on the similarity between two texts. Objective is to write a program that takes as inputs two texts  and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0.

# In[1]:


# Loading libraries
import re
import io
import nltk
#nltk.download()
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


# ### Reading the Sample Files

# In[2]:


def text_to_string(file):
    with open(file, 'r') as f:
        data = f.read()
        words = data.split()
        words = [word.lower() for word in words]
    return words


# ### Removing Punctuations

# In[3]:


def punctuation(string): 
  
    for x in string:
        if x in punctuations: 
            string = string.replace(x, "") 
    return string


# ### Removing Stop-Words

# In[4]:


def stop_words(string_list):
    string_list = [x for x in string_list if x not in stopwords]
    return string_list


# ### Calculating the Jaccard similarity, by comparing the ratio of the number of overlapping words between two texts to the total number of unique words in the text. 
#     Documents that are exactly the same will get a score of 1, and documents that don’t have any words in common will get a score of 0

# In[5]:


def jaccard_similarity(str1, str2): 
    string_set1 = set(str1) 
    string_set2 = set(str2) 
    string_intersection = string_set1.intersection(string_set2)
    return round(float(len(string_intersection)) / (len(string_set1) + len(string_set2) - len(string_intersection)),4)


# In[6]:


def text_similarity(sample1,sample2):
    string_1 = text_to_string(sample1)
    string_2 = text_to_string(sample2)
    string_list1 = punctuation(string_1)
    string_list2 = punctuation(string_2)
    string_text1 = stop_words(string_list1)
    string_text2 = stop_words(string_list2)
    return jaccard_similarity(string_text1,string_text2)


# In[7]:


print("The similarity score of Sample 1 & Sample 2 is:",text_similarity('sample1.txt', 'sample2.txt')) 


# In[8]:


print("The similarity score of Sample 1 and Sample 3 is:",text_similarity('sample1.txt', 'sample3.txt')) 


# ### Conclusion
#     Sample text 1 and Sample text 2 are much more similiar as compared to Sample text 1 and Sample text 3
