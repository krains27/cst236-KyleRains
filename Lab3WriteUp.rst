=============
Lab3 Write-up
=============


What are five examples of other testing(nose2) plugins that might be useful?
============================================================================

Buffering test output (allows me to see stdout/stderr in test report)
FailFast (stops after first error)
log capture (appends captured log messages to error reports)
I would like to write a plugin that compares the amount of test run to the amount of 
tests written (in case their are tests with the same name)
A plugin that would notify you if there are functions that aren't preceded with test
(in case I didn't mean to not add test)

Do you plan to create any of these plugins for your term project?
=================================================================

Some of these plugins already exist, but I would consider creating the last two since these are
issues that have plagued me. 

What is the hardest part of this lab?
=====================================

Creating and running the plugin was the most difficult since it was my first time being exposed
to this. 

Did the code fully and completely implement the requirements? Explain
=====================================================================

No. Requirements 0018, and 0017 returned a different answer than  expected. 

Was the requirements complete? Explain
======================================

No. 0006 should have specified what was used to determine the match percentage (was it number of correct letters?), 0007
didn't specify the number format (was it hex, octal, decimal). 0018 should have specified the format of the date/time. 

Bug Requests
============

**ISSUE Number:** 0001

BRIEF: Number not removed if at end of string

Steps to reproduce:: Ask question with a number just before 0x3e (How are you 3>)

Comments: This should have been covered by requirement #0007

Time Spent: 10 min




**ISSUE Number:** 0002

BRIEF: Hex number not removed from question string

Steps to reproduce:: Ask question with a number formatted in hex within the question (What is 0x55 feet in miles>)

Comments: This should have been covered by requirement #0007

Time Spent: 10 min



**ISSUE Number:** 0003

BRIEF: Octal number not removed from question string

Steps to reproduce:: Ask question with a number formatted in octal within the question (What is 0o55 feet in miles>)

Comments: This should have been covered by requirement #0007

Time Spent: 10 min



**ISSUE Number:** 0004

BRIEF: Response to question which converts feet to miles does not append miles to the answer

Steps to reproduce:: Ask the question: What is <float> feet in miles> to get the incorrect response

Comments: This should have been covered by requirement #0017

Time Spent: 10 min


**ISSUE Number:** 0005

BRIEF: Response to question which returns number of seconds since <date> only returns 42 seconds

Steps to reproduce:: Ask the question: How many seconds since <date time> to get the incorrect response

Comments: This should have been covered by requirement #0018

Time Spent: 10 min


**ISSUE Number:** 0006

BRIEF: Each question that is checked against entered question is printed to the screen. 

Steps to reproduce:: Ask a valid question, and record what is printed to the screen. 

Comments: It seems unnecessary to print each comparison question to the screen. 

Time Spent: 10 min


Why are requirements tracing so important?
==========================================

Tracing requirement allows you to see what requirements were actually tested and what requirments
still need to be tested. 

How long did it take to complete this lab?
==========================================

It took me about three hours to complete this lab. Most of the hang up was on creating the plugin. 