=============
Lab5 Write-up
=============


What was the hardest part of this lab?
======================================

The hardest part for me was determining how to fit in each type of perfomance test.  

What is the difference between performance testing and performance measurement?
===============================================================================

Performance testing is testing a project based on the performance requirements. Performance measurement is the 
result of testing performance in different conditions. Then plotting the data to get a visual representation
of the measurement.

What new bugs did you encounter with the new code?
=========================================================================

The closest thing I found for a bug was during the storage/retrieval requirements. I noticed that the 
5 ms storage and retrieval weren't met when the system had 1 million+ question/answer pairs. However, 
I didn't submit a bug report about this since I noticed that the times were met during my isolation testing 
where I attempted to store and retrieve questions using the dictionary instead of the ask function. 

Did you mock anything to speed up performance testing? Do you see any issues with this?
=======================================================================================

No I didn't mock anything new in this lab. I see this being an issue because performance testing needs 
to account for all the timing and resources that the system would normally go through. 

Generate at least 5 performance measurement value sets and graphs (these sets must be worthwhile)
=================================================================================================

I completed this using matplotlib

Explain Load Testing, stress testing, endurance testing, spike testing configuration testing and isolation testing. How did you implement each of these?
========================================================================================================================================================

Load testing is testing a certain functionality while it is under a specific load. I implemented this by teaching new answers
and asking questions while the system was under a load (adding 1 million question/answer pairs to the dict). Stress testing is 
basically the same as load testing except that it is used to test safety concerns. I didn't implement a stress test since there
are no known safety concerns and load testing will suffice for this purpose. Endurance testing is testing the systems ability
to function over time. I implemented this by asking the questions associated with the new requirements that I added 10000 times. 
Spike testing is testing system performance for a specific load, spiking the load way above the previous load, and then spiking 
back down to the previous load. I implemented this by asking a set of questions 10 times, spiking the question/answer pairs
to over 1000000 and asking the same question 10 times. Then spiking back to original value, and asking the questions 10 times.
Isolation testing is isolating a specific part of the system to ensure that it meets its performance requirements. I implemented this
by isolation the dictionary operations for the store and retrieve functionality.