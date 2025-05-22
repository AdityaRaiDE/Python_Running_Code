1. Integer :-> 
          -> Int type 
          -> exact representation 
          -> can be of any mangnitude 
          -> created from literals , can have all +ve and -ve number 
          -> so Integer can be generated in memeory either by literals or by expression or by calculation
2. Float :->
          -> Float Type
          -> decimal 
          -> Not all floats have finite representation in python or not only in python it can be in all programming language 
          -> ex :-> 0.1+0.1+0.1 == 0.3 evaluates to False 
          -> so pay caution while using equality operator while comapring decimals or floats 
          -> formar(0.1,'.25f'):-> value will be lagrer than 0.1 
          -> so if we want to check if any float has finite representation or not then use format(flat,'0.54f') if zero coming at the end it means it is getting 
             represented finitly 

-----------------------------=======================================================================================================---------------------------
objects :->
          -> entities created by python to store values and functionality 
          ->  objects has state and functionality . state is called data attributes and functionality is called method attributes 
          -> Int is an object 
           -> its value is state or data attribute . 
           ->  it can be added , multiplied , substracted are its functioanlity or method attributes 
           -> it also has visual representation it means when we print them on termianl how it looks is also defined 
          -> data types in python are mutuable and immutable , if one of data attributes of the objcet can be changed then it is called mutable and if none of
             data attributes can be changed then it is called immutable 
--------------------======================================================================================================================------------------
Variables :->
          -> case senstive , use _ and letter as starting char , should not be reserved word 
          -> use snake case ( account_balance)
          -> = is assignment operator , in this case rhs is evaluated fully and then python creates a object in memeory and then the lhs will start referring to
            memeory address of that object . 
          -> so variable is just a way of naming object so that we can remember them in pur whole program and the value can be reffered any time by its name 
          -> so in python we tell a variable is refeering  or pointing to a variable 
-----------------------=====================================================================================================================-------------
Airthmetic operators :->
          -> it is programming symbol to perform certain operations on object 
          -> operator works on objects and these objects are called operands 
          -> airhtmetic , logical , comparision/relational operator 
          -> if no of operand is 1 then it is uninary operator and if 2 then binary and if 3 then it is ternary operator
          -> so operand is immutable then operator will return new object and if it is mutualble then it can modify the same object 
          -> _ , + :-> uninary , 
          -> airtmetic operators mainly work on int , float and str
          -> Int can be added to Float bt Int cannot be added to str .
          -> / and // is float and integer division
          -> 2 **(-4) :-> 1 / (2*2*2*2)
          -> ** can return float as well as int , if power is +ve it returns int and if -ve then it returns float 
          -> a + b :-> (a).__add__(b) gets evaluated as 
          -> so each operator symbol is associated with special or magic methods and it is done by python automatically and it should be implemented in the class
             then only we can use that .
          -> comparsion/relational operators are == , >,<,>=,<=, !=. logical operators are (and,or,not) and all gets evaluated to either ture or false &
             operands should be comparable 
          ->  Imp :-> == returns False if operands are not comparable but other retuns Exception (TypeError) in case of logical operators 
          -> 10 == 'aditya',10 != 'aditya' :-> returns True & False .. 10 > 'aditya',10 >= 'aditya',10 <'aditya',10 <= 'aditya' ( TypeError) 
          -> always use () to avoid precedence 
          -> integer division is floor division of float division .
          -> negtaive value complicate the things for divison , mod and divmod so use it with caution
          ->  a / b == a // b + ( a % b) / b 
          ->  a % b = a - b( a // b) or do this  a % b = a - b ( floor( a / b))) this is the besr way to do 
-------------============================================================================================================================------------
----------> is vs == 
         "is returns True if both lhs and rhs refer to the same object in memory (same memory address), and == returns 
              True if the values or contents of lhs and rhs are the same."
----------> is is called identity operator ,it comapres the id of 2 objects 
----------> == gets implemented by __eq__ or __neq__
---------->  (in and not in ) is membership operator , to find elements in the collection .It is implemneted by __contains__(self, item)
----------> if __contians__ not implemented then it looks for __iter__ and __eq__
-------------============================================================================================================================------------
---Booleans 
------- bool type 
------- only 2 values True/False 
------- short circuit evaluation
---=================================================================================================================================-------------
 -- if (True) 
-- nested if 
--  else is optional block 
-- if-elif-else (lader)
-- if 
-- if-else
-- if--if--else--else 
--- (Ternary if (inline or one-liner if-else))lhs = true_result if conditon else false_result































