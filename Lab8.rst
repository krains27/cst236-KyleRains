Lab 8 Write Up
--------------

How was this test useful?
=========================

This test allowed me to find issues in python modules that were in a given directory. I found import errors, 
function parameter errors, and class member errors. Running this would allow me to see problems after I
pushed new changes to a branch. 

How did you report errors found by this test? How difficult would it be for a developer to debug these errors
=============================================================================================================

For importing modules, I displayed the module that was being imported the exception that was raised, and the 
exception message. For instantiating a class, I displayed the module the class was in, the class that failed, 
the exception and the exception message. For functions and members, I displayed the class or module 
function/member was in, the exception that was thrown and the exception message. I think this amount of 
detail would make it easy for a developer to debug. 

What other things would be useful to have in a sanity test?
===========================================================

I would have added calling properties, checking init values after instantiation, and UI testing.

How would you sanity test a UI? A database interface? a webpage? a C# program?
=========================================================================================

I would test a UI by pressing a known set of buttons and ensuring that the next page displayed correctly. I would test
a database interface ensuring I can connect to a test database, make reads/writes to a database and disconnect to
the database. I would test a webpage by pressing buttons and entering text where it should be allowed. I would test a c#
program by importing a namespace, instantiating a class, or classes, and making calls to known functions of the classes. 