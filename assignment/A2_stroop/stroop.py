import time
import sys
import os
import random
from psychopy import visual,event,core,gui
from generate_trials import generate_trials
from helper import import_trials, getRuntimeVariables, create_data_file, write_to_file

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

# get runtime variables
order = ['subj_code', 'seed', 'num_reps']
runtime_vars_template = {'subj_code':'stroop_101', 'seed': 101, 'num_reps': 25}
runtime_vars = getRuntimeVariables(runtime_vars_template, order=order)

#generate trials
generate_trials(runtime_vars['subj_code'], runtime_vars['seed'], runtime_vars['num_reps'])

#list of all trials
trials_list = import_trials(f"trials/{runtime_vars['subj_code']}_trials.csv")

#file handler for incoming responses
data_file = create_data_file(runtime_vars['subj_code'])

for idx, cur_trial in enumerate(trials_list):
    trial_num = idx + 1 # keep track of 1-index trial number
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
    
    #set trial properties based on current trial from trials_list
    cur_word = cur_trial['word']
    cur_color = cur_trial['color']
    cur_trial_type = cur_trial['trial_type']
    cur_orientation = cur_trial['orientation']

    #display each stim for 1.0 sec
    word_stim.setText(cur_word)
    word_stim.setColor(cur_color)
    if cur_orientation == "upside_down": 
        word_stim.setOri(180)
    else: 
        word_stim.setOri(0)
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
        response = [trial_num, "NA", 0, "More than 2000"]
        write_to_file(data_file, cur_trial, response)
        
    elif key_pressed[0][0] != 'q':  
        rt = key_pressed[0][1]*1000 # convert to ms
        RTs.append(rt)
        is_correct = 1 if key_pressed[0][0] == cur_color[0] else 0
        response = [trial_num, key_pressed[0][0], is_correct, rt]
        write_to_file(data_file, cur_trial, response)
        #if wrong, give feedback
        if is_correct == 0:
            feedback_incorrect.draw()
            win.flip()
            core.wait(1)

    elif key_pressed[0][0] == 'q':
        break

print(RTs)
win.close()
core.quit()
        
