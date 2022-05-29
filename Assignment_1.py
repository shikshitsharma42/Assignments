#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment01

1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.

*       -  It is an expression.
'hello' -  It is a value.
-87.8   -  It is a value.
-       -  It is an expression.
/       -  It is an expression.
+       -  It is an expression.
6       -  It is a value.2. What is the difference between string and variable?

Ans- A string can be made up of using characters, letters, phrases, symbols and even numbers enclosed in double quotes or single quotes whereas Variable is used to store data and it's first letter can not be integer or special. e.g.-

     "Shikshit" , '42Ineuron' , 'shikshitsharma42' - All these can be identified as string.
     
     42Ineuron , 123sharma , @sharma - All these can not be taken as variable(will giva syntax erro). 3. Describe three different data types.

Ans- (I) int data type - 
            This int data type is a type of data type which is used when we want our data should be or is integer(in number).
            e.g  -  int('any data')
            
     (II) dict data type - 
             In dictionary data type, curly braces{} is used data is kept in curly braces in the form of key-value pair.
            e.g  -  d = {"key1":"value1","key2":"value"}
             
    (III) set - 
             In this data type also curly braces is used but not in key-value pair.
            e.g  -  s = {1,2,3,4,9}4. What is an expression made up of? What do all expressions do?

Ans- An expression can be made up of operators and operands or values or variables etc. 
        e.g -    c = a + b  (Here c,a and b are operands and = ,+ are operators)
      All expressions are used to perform or evaluate some tasks defined by the operators and also used to assign values.5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?

Ans- An expression evaluates based on the operators wheres as A statement always does whatever the statement says like print("hello"), here is simply print the statement whereas in spam = 10, the value 10 is assigned to variable spam using the (=) operator.6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1

Ans - 237. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3

Ans-  'spam' + 'spamspam' -  'spamspamspam'
      'spam' * 3          -  'spamspamspam'8. Why is eggs a valid variable name while 100 is invalid?

Ans - This is because we can not take the first letter of the variable name as integer or number or some special number and
      here 100 consists 1(integer) on it's first postion.9. What three functions can be used to get the integer, floating-point number, or string version of a value?

Ans-  for integer -  int()
      for floating - float()
      for string -   str()10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'

Ans - This will give error as we can only concatenate string to string not integer to string.
      It can be fixed by Typecasting the integer part(99) to string in the expression as follows -
              
 'I have eaten ' + str(99) + ' burritos.'      or     'I have eaten ' + '99' + ' burritos.'

       
       Now it will not give error.