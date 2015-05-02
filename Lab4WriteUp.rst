=============
Lab4 Write-up
=============


What observations did you make while performing the analysis on the system?
===========================================================================

I noticed that the CC and MI scores stayed the same. The requirement completeness increased 
along with the requirement coverage. The known and new defects decreased as well. 

What are the advantages/disadvantages of performing this analysis?
==================================================================

The advantages were that I was able to see the trends for the code and tests. The disadvantage 
was that I think that some of the analysis could lead to a false sense of security (just 
because there aren't any known bugs, doesn't mean that there aren't any bugs).

What are the advantages of data mutation? Did you use any of these tools?
=========================================================================

Data mutation provides a way to test tests. If you have a test that can't fail, then
it really isn't testing anything. Data mutation will provide you a way to see if your
test can fail.  

What did you use Mock for in this lab?
======================================

I used Mock for Popen, the socket calls in get_other_users, and for the calls to random. 

How long did this lab take to complete?
=======================================

Too long (~6 hrs). I got hung up with a misunderstanding on how Mock worked. 