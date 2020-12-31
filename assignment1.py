#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# For this assignment you are welcomed 
# to use other regex resources such 
# a regex "cheat sheets" you find on the web. 
# Feel free to share good resources with your peers in slack!
# 
# 


# ## Part A
# 
# Find a list of all of the names in the following string using regex.



import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    result = [s for s in re.split("([A-Z][^A-Z*])", simple_string) if s]
    raise NotImplementedError()

assert len(names()) == 4, "There are four names in the simple_string"


# ## Part B
# 
# The dataset file in [assets/grades.txt](assets/grades.txt) contains a line separated list of people with their grade in 
# a class. Create a regex to generate a list of just those students who received a B in the course.


def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()

    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


assert len(grades()) == 16


# ## Part C
# 
# Consider the standard web log file in [assets/logdata.txt](assets/logdata.txt). This file records the access a user makes when visiting a web page (like this one!). Each line of the log has the following items:
# * a host (e.g., '146.204.224.152') 
# * a user_name (e.g., 'feest6811' **note: sometimes the user name is missing! In this case, use '-' as the value for the username.**)
# * the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
# * the post request type (e.g., 'POST /incentivize HTTP/1.1' **note: not everything is a POST!**)
# 
# Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:
# ```
# example_dict = {"host":"146.204.224.152", 
#                 "user_name":"feest6811", 
#                 "time":"21/Jun/2019:15:45:24 -0700",
#                 "request":"POST /incentivize HTTP/1.1"}
# ```

# In[ ]:


def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
    
    # YOUR CODE HERE
    raise NotImplementedError()


assert len(logs()) == 979

one_item={'host': '146.204.224.152',
    'user_name': 'feest6811',
    'time': '21/Jun/2019:15:45:24 -0700',
    'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"

