=============
Lab2 Write-up
=============


Explain the major differences between TDD and BDD
=================================================

TDD relies on the developer to create tests before writing code. There is a defined cycle of write tests, run test,
fix failures (by implementing code), run tests again, repeat. BDD relies on this same concept of tests first, but BDD 
uses natural language to define test cases as opposed to TDD which will have a developer just write the tests. 

What is a mixin, what challenges can occur when testing them? What order are they initialized in
================================================================================================

A mixin is python's version of multiple inheritance. Some of the challenges are mixins provide methods
but not attributes, and their is no diamond inheritance hierarchy. Mixins are initialized right to left. 

In python what does "super" do?
===============================

Super allows you to call up to the parent class without calling the class explicitly. 

Was there any job stories that did not meet the criteria we discussed in class? How did you handle this case?
=============================================================================================================

Yes there were a number of job stories that were as clear as mud, especially in the BDD section. To handle these
I had to make assumptions. This is the potential problem with job stories, is that there are a number of things
that can be left to interpretation. 

Which model did you find most challenging? Why?
================================================

The BDD model was more challenging. I have never used BDD before, so there was a slight learning curve
to understand it. Once I did though, it did get a little easier. 

Which model did you find easiest to update/maintain?
====================================================

I feel that the TDD model would be easier to update/maintain because I didn't have a separate file, like the .feature files, that I had to maintain
on top of my tests and code. 

How did you test that logging occurred only when desired?
=========================================================

I used pip to install testfixtures. This provided a module called LogCapture. With this module, all I had to do was invoke a log 
capture object at the start of my test, and then I called check on the LogCapture object while passing check my expected log 
source, level, and message. 