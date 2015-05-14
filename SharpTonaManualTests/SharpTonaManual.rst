**Verify Title Manual Test (Requirement #0001)**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Look in the upper left hand corner of the SharpTona window
#. Verify the title is "SharpTona"
#. Close sharpTona.exe by clicking the red x in the top right hand corner

**Verify Label Manual Test  (Requirement #0002)**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Look on the main SharpTona form
#. Verify the top label has the text "Question:"
#. Verify the bottom label has the text "Answer:"
#. Close sharpTona.exe by clicking the red x in the top right hand corner

**Receive an answer Manual Test (Requirement #0003)**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Enter the string "How are you?" in the text box following the label "Question:"
#. Press the button labeled "Ask"
#. Verify the text "I don't know please teach me." appears in the text box following the label "Answer:"
#. Close sharpTona.exe by clicking the red x in the top right hand corner

**Default Question/Answer Manual Test (Requirement #0004)**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Enter the string "What is the answer to everything?" in the text box following the label "Question:"
#. Press the button labeled "Ask"
#. Verify the text "42" appears in the text box following the label "Answer:"
#. Close sharpTona.exe by clicking the red x in the top right hand corner

**Disabled Objects Manual Test (Requirement #0005)**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Locate the buttons labeled "Teach" and "Correct" in the bottom right hand corner. 
#. Verify each of the buttons are disabled (they are greyed out).
#. Verify the text box following the label "Answer:" is disabled (it is greyed out).
#. Close sharpTona.exe by clicking the red x in the top right hand corner

**Display Answers Manual Test (Requirement #0006)**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Enter the string "What is the answer to everything?" in the text box following the label "Question:"
#. Press the button labeled "Ask"
#. Verify the text "42" appears in the text box following the label "Answer:"
#. Close sharpTona.exe by clicking the red x in the top right hand corner

**No Question Manual Test (Requirement #0007)**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Verify the text box following the label "Question:" is empty 
#. Press the button labeled "Ask"
#. Verify the text "Was that a question?" appears in the text box following the label "Answer:"
#. Close sharpTona.exe by clicking the red x in the top right hand corner

**Known Question Manual Test (Requirement #0008)**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Enter the string "What is the answer to everything?" in the text box following the label "Question:"
#. Press the button labeled "Ask"
#. Verify the text "42" appears in the text box following the label "Answer:"
#. Verify the text box following the label "Answer:" is enabled (it is not greyed out).
#. Verify the text box following the label "Answer:" allows user input by double-clicking in the text box and typing "test".
#. Close sharpTona.exe by clicking the red x in the top right hand corner

**Correct Button Manual Test (Requirement #0009)**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Enter the string "What is the answer to everything?" in the text box following the label "Question:"
#. Press the button labeled "Ask"
#. Verify the text "42" appears in the text box following the label "Answer:"
#. Enter the string "Nobody knows the answer to everything." in the text box following the label "Answer:"
#. Press the button labeled "Correct"
#. Verify the text box following the label "Answer:" is disabled (it is greyed out).
#. Verify the button labeled "Teach" is disabled (it is greyed out).
#. Verify the button labeled "Correct" is disabled (it is greyed out).
#. Press the button labeled "Ask"
#. Verify the text "Nobody knows the answer to everything." appears in the text box following the label "Answer:"
#. Verify the button labeled "Teach" is disabled (it is greyed out).
#. Verify the button labeled "Correct" is enabled (it is not greyed out).
#. Close sharpTona.exe by clicking the red x in the top right hand corner

**Teach Button Enable Manual Test (Requirement #0010)**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Enter the string "Who are you?" in the text box following the label "Question:"
#. Press the button labeled "Ask"
#. Verify the text "I don't know please teach me." appears in the text box following the label "Answer:"
#. Verify the button labeled "Teach" is enabled (it is not greyed out).
#. Close sharpTona.exe by clicking the red x in the top right hand corner

**Teach Button Teach an Answer Manual Test (Requirement #0011)**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Enter the string "Who are you?" in the text box following the label "Question:"
#. Press the button labeled "Ask"
#. Verify the text "I don't know please teach me." appears in the text box following the label "Answer:"
#. Verify the button labeled "Teach" is enabled (it is not greyed out).
#. Highlight the text in the text box following the label "Answer:" and enter the string "I am Groot" into the text box
#. Press the button labeled "Teach"
#. Verify the text box following the label "Answer:" is disabled (it is greyed out).
#. Verify the button labeled "Teach" is disabled (it is greyed out).
#. Verify the button labeled "Correct" is disabled (it is greyed out).
#. Press the button labeled "Ask".
#. Verify the text "I am Groot" appears in the text box following the label "Answer:" 
#. Verify the button labeled "Teach" is disabled (it is greyed out).
#. Verify the button labeled "Correct" is enabled (it is not greyed out).
#. Close sharpTona.exe by clicking the red x in the top right hand corner