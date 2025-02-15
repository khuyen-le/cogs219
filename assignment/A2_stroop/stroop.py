import time
import sys
import os
import random
from psychopy import visual,event,core,gui

stimuli = ['red', 'orange', 'yellow', 'green', 'blue']

win = visual.Window([800,600],color="gray", units='pix',checkTiming=False)
placeholder = visual.Rect(win,width=180,height=80, fillColor="lightgray",lineColor="black", lineWidth=6,pos=[0,0])
#maybe should also autoDraw placeholder? 
word_stim = visual.TextStim(win,text="", height=40, color="black",pos=[0,0])
instruction = visual.TextStim(win,text="Press the first letter of the ink color", height=20, color="black",pos=[0,-200])
instruction.autoDraw = True

fixation = visual.TextStim(win,text="+", height=15, color="black",pos=[0,0])

response_keys = ['r', 'o', 'y', 'g', 'b', 'q'] #'q' to escape

while True:
    # display fixation cross for 500ms
    placeholder.draw()
    instruction.draw()
    fixation.draw()
    win.flip()
    core.wait(0.5)

    # wipe fixation cross
    placeholder.draw()
    instruction.draw()
    win.flip()
    core.wait(0.5)
    
    #choose randomly from stimuli list
    cur_stim = random.choice(stimuli)
    
    #display each stim for 1.0 sec
    word_stim.setText(cur_stim)
    word_stim.setColor(cur_stim)
    placeholder.draw()
    instruction.draw()
    word_stim.draw()
    win.flip()
    
    #get the first key press
    response = event.waitKeys(keyList=response_keys)[0] 
    if response != 'q': 
        #continue to next stim
        placeholder.draw()
        instruction.draw()    
        win.flip()
        core.wait(.15)
    if response == 'q':
        win.close()
        core.quit()
        
