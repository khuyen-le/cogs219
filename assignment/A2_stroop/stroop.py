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
RTs = [] #store response times

responseTimer = core.Clock()

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

    #clear timer to wait for response
    event.clearEvents()
    responseTimer.reset()
    key_pressed = event.waitKeys(keyList=response_keys, timeStamped=responseTimer)
    if key_pressed[0][0] != 'q':  
        print(key_pressed[0])    
        rt = key_pressed[0][1]*1000 # convert to ms
        print(rt)
        RTs.append(rt)
        #continue to next stim
        placeholder.draw()
        instruction.draw()    
        win.flip()
        core.wait(.15)
    if key_pressed[0][0] == 'q':
        win.close()
        core.quit()
        
