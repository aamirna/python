#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This function counts tabs in the text
def count_tabs(text):
    return text.count("\t")

#This function counts lines in the text
def count_lines(text):
    return text.count("/n")

#This function counts words in the given text
def count_words(text):
    return len(text.split())

#This function counts sentences in the given text
def count_sentences(text):
    if text[-1] == ".":
        return len(text.split(".")) - 1
    else:
        return len(text.split("."))
    
#This function remove whitespaces (if more than one consecutive) from the given text
def remove_white_spaces(text):
    return " ".join(text.split())

#This function removes punctuation symbols from the given text.
def remove_punctuations(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    output_text = text
    for punctuation in punctuations:
        output_text = output_text.replace(punctuation, "")
    return output_text



# In[ ]:




