=============
Lab1 Write-up
=============


What was the hardest part of this lab?
======================================

I spent the most time trying to get my CI build to install the nose2-cov requirement
during the pip install on the workspace.  

During the course of this lab, why did we exclude .pyc files?
=============================================================

.pyc is a the compiled python files. Binaries like the .pyc files should not be included in a 
commit because a binary file undergoes a high percentage of change each time python code is 
compiled. This could be an issue because git only stores deltas of files. 

Name three files which would likely need to have a gitignore added?
===================================================================

.pyc, .exe, and bitmaps. 

What is a pyunit TestCase?
==========================

This is the smallest unit of testing. A testcase should check for a specific result based
off a known set of inputs. 

What is the difference between a git cherry pick and a rebase?
==============================================================

A cherry pick allows you to apply the changes from an existing commit to the current branch. A rebase 
allows you to integrate changes from one branch to another. A rebase is good if you have changes on a
current branch that you want to integrate into master. 

How could you use git to print out just the author name of a given file for the current version of the repo?
============================================================================================================

git log -1 --pretty=format:"%an" <given file>

During this lab did you explore Tortoise Git or GIT Extensions? If not take a look at them, they probably would be useful for the remainder of the class
========================================================================================================================================================

Yes I used tortoise git along with the command line.

Did you find the second issue in get_triangle_type? Did you choose to test the code as is or fix the code in get_triangle_type?
===============================================================================================================================

Yes I found the second issue with assigning values from the list. I fixed this before I tested the code. 