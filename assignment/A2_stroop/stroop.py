import time
import sys
import os
import random
from psychopy import visual,event,core,gui

stimuli = ['red', 'orange', 'yellow', 'green', 'blue']
trial_types = ['congruent', 'incongruent']

win = visual.Window([800,600],color="gray", units='pix',checkTiming=False)
placeholder = visual.Rect(win,width=180,height=80, fillColor="lightgray",lineColor="black", lineWidth=6,pos=[0,0])
#maybe should also autoDraw placeholder? 
word_stim = visual.TextStim(win,text="", height=40, color="black",pos=[0,0])
instruction = visual.TextStim(win,text="Press the first letter of the ink color", height=20, color="black",pos=[0,-200])
instruction.autoDraw = True

fixation = visual.TextStim(win,text="+", height=15, color="black",pos=[0,0])
feedback_incorrect = visual.TextStim(win,text="INCORRECT", height=40, color="black",pos=[0,0])
feedback_slow = visual.TextStim(win,text="TOO SLOW", height=40, color="black",pos=[0,0])

response_keys = ['r', 'o', 'y', 'g', 'b', 'q'] #'q' to escape
RTs = [] #store response times

responseTimer = core.Clock()

def make_incongruent(cur_color): 
    """Return a random color that is different from the color passed in. 
    :Parameters:
        cur_color : string
            Current color of the stimuli
    """
    #list comprehension solution from assignment code!
    #much better than my original solution, 
    #which is to randomly choosing from the full stimuli list in a while loop and hope for the best...
    incongruent_colors = [stim for stim in stimuli if stim != cur_color])
    return random.choice(incongruent_colors)

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
    
    #choose randomly from stimuli list and trial types
    cur_word = random.choice(stimuli)
    cur_trial_type = random.choice(trial_types)

    #display each stim for 1.0 sec
    word_stim.setText(cur_word)

    if cur_trial_type == 'incongruent': 
        cur_color = make_incongruent(cur_word)
    else: 
        cur_color = cur_word

    word_stim.setColor(cur_color)
    placeholder.draw()
    instruction.draw()
    word_stim.draw()
    win.flip()

    #clear timer to wait for response
    event.clearEvents()
    responseTimer.reset()
    key_pressed = event.waitKeys(maxWait=2, 
                                 keyList=response_keys, 
                                 timeStamped=responseTimer)
    if not key_pressed: 
        feedback_slow.draw()
        win.flip()
        core.wait(1)
        
    elif key_pressed[0][0] != 'q':  
        rt = key_pressed[0][1]*1000 # convert to ms
        print(rt)
        RTs.append(rt)
        #if wrong, give feedback
        #cur_color instead of cur_word!
        if key_pressed[0][0] != cur_color[0]: 
            feedback_incorrect.draw()
            win.flip()
            core.wait(1)
        #continue to next stim
        #placeholder.draw()
        #instruction.draw()    
        #win.flip()
        #core.wait(.15)
    elif key_pressed[0][0] == 'q':
        win.close()
        core.quit()
        
