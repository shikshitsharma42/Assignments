#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment02

1.What are the two values of the Boolean data type? How do you write them?

Ans - Two values are -  True
                        False
                        
       The very first letter of these values should be Capital otherwise it will not take it as a boolean data type. So it is          always written as first letter capital and remaining be small letters.2. What are the three different types of Boolean operators?

Ans - Three Boolean operators are - or , and , not3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).

Ans - Truth Table for or Operator: 

Conditon1	Condition2	Output       The or operator gives True(1) as output if either condition is true, it only give False(0)
  0	            0	      0          when both the conditions are false.
  0	            1	      1
  1	            0	      1
  1	            1	      1
  
  
      Truth Table for and Operator:
      
Conditon1	Condition2	Output       The and operator gives True(1) only if both statements/condtions are true. If either of 
  0	            0	      0          the condition is false then output will be False(0).
  0	            1	      0           
  1	            0	      0
  1	            1	      1
      
      
      Truth Table for not Operator:
      
Condition 	Output                   The not operator reverses the input, if condtion is True(1) it gives False(0) and vice-
  0           	1                    versa.
  1             0
  



4. What are the values of the following expressions?
(5 > 4) and (3 == 5)                    - False 
not (5 > 4)                             - False
(5 > 4) or (3 == 5)                     - True
not ((5 > 4) or (3 == 5))               - False
(True and True) and (True == False)     - False
(not False) or (not True)               - True5. What are the six comparison operators?

Ans -  1) <      -    Less than 
       2) >      -    Greater than
       3) <=     -    Less than or equal to
       4) <=     -    Greater than or equal to
       5) ==     -    Equal to
       6) !=     -    Not Equal to6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.

Ans -  Equal to operator is denoted by the '==' sign and is used to compare two condtions whereas 
       Assignment operator is denoted by the '=' sign and is used to assign some values to a variable.7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

Ans -  First Block -   spam = 0
                       if spam == 10:
                       print('eggs')
                       
       Second      -   if spam > 5:
                       print('bacon') 
                       
       Third       -   else:
                       print('ham')
                       print('spam')
                       print('spam')8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.
# In[4]:


spam = int(input("Enter the Number = "))
if spam == 1 :
    print("Hello")
elif spam == 2 :
    print("Howdy")
else :
    print("Greetings!")

9.If your programme is stuck in an endless loop, what keys you’ll press?

Ans -  CTRL+C10. How can you tell the difference between break and continue?

Ans - break eliminates the execution of remaining iteration of the loop and continue will terminate the current iteration             of loop.11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

Ans - These all contains elements starting from 0 (as lower bound) to 9 (10 is upper bound so it will exclude it).
      All these are same as lower bound in all is 0 , upper bound as 10 and step size or jump size by default in
      range(10) and range(0,10) be 1 wheres in range(0,10,1), it is also given as 1.
      The outcome of these range functions are same as follows-
# In[1]:


for i in range(10):
    print(i)


# In[3]:


for i in range(0,10):
    print(i)


# In[4]:


for i in range(0,10,1):
    print(i)

12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.
# In[5]:


#Using for loop

for i in range(1,11):
    print(i)


# In[6]:


#Using while loop

a=1
while a in range(1,11):
    print(a)
    a=a+1

13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?

Ans - We will call it by using the following syntax.

           spam.bacon()