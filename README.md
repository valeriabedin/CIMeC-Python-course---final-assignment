# CIMeC-Python-course---final-assignment

The script I am using here was taken from the Cajal Experimental Neuroscience - Neurokit course. 
The reference of the original scripts can be found at the following link:
https://github.com/NoBlackBoxes/LastBlackBox/tree/master/course/bootcamp 

This project aimed to build a robot, Ambrogio for friends :)  
that mimicks the basic aspects of a vertebrate's brain.
Together with my team we made the robot move and implemented audio/vision sensors that eventually enabled face recognition.
We wanted Ambrogio to behave like a mouse: explore the environment in the dark, freeze when the light is on, and check for danger. 
We decided to use faces as a stimulus for triggering a "run away" response. 

Regarding the script I use here, I focused on the audio input to the left ear of the robot. 
The uploaded file: 
record - original script 
is the script I took for this assignment.
I changed some parameters of the recording and made it print only the data referring to the left ear.
The output of this code are printed as a txt file:
interleaved_data

Then I made a script to plot the sound trace recorded over time.
