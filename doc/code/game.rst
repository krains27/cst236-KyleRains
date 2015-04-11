Game
====

Game provides functions for describing a game to defend a fortress against orcs. 

Game Commands
^^^^^^^^^^^^^
There are a number of game commands that will allow you to play the game; however, since this
game is not the final solution, I will cover some of the commands that the game would allow

.. note:
    This game cannot be played in its current state, but these are the commands that 
    would be used if it could. 
    
Check Perimeter
^^^^^^^^^^^^^^^
Entering P at the prompt will allow the game to check if any orcs have breached the 
perimeter. This will display a message if the perimeter was indeed breached. 

Stopping the Game
^^^^^^^^^^^^^^^^^
Entering X at the prompt will stop the game. Currently it simply displays a message that 
the game has ended. 

Displaying Orcs' Distances
^^^^^^^^^^^^^^^^^^^^^^^^^^
Entering D at the prompt will list the distances of all the current orcs in the unit format 
desired. 

Displaying Orcs' Velocities
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Entering V at the prompt will list the velocities of all the current orcs in the unit format 
desired. 

Displaying Orcs' Types
^^^^^^^^^^^^^^^^^^^^^^
Entering T at the prompt will list the types of all the current orcs.

Removing Orcs
^^^^^^^^^^^^^
Entering R at the prompt will allow you to remove a given orc. You will be prompted for the orc's id
after R has been entered. 

Setting Units
^^^^^^^^^^^^^
Entering U at the prompt will allow you to select the units of measure to display. These units
can be set to Imperial, Metric, Parsecs, or Nautical

Setting Priority
^^^^^^^^^^^^^^^^
Entering PR [ID] [Priority] at the prompt will allow you to set the given priority to the 
orc with the given ID.

Displaying Details of Specific Orcs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Entering OD [ID] at the prompt will list the attributes (distance, velocity, type, ID and priority) of the orc with the given ID. 

Generating Orcs
^^^^^^^^^^^^^^^
Entering G at the prompt will generate 5 orcs with random attributes.

Winning when Bored
^^^^^^^^^^^^^^^^^^
Entering ENTer the Trees at the prompt will clear all orcs and allow you to win. 

Displaying Commands
^^^^^^^^^^^^^^^^^^^
Entering ? at the prompt will list all the available commands while playing the game. 

Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.game
    :members: