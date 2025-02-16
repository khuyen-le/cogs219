import time
import sys
import os
import random
from psychopy import visual,event,core,gui
from generate_trials import generate_trials

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

def getRuntimeVariables(runtime_vars, order, exp_title='Stroop'):
    dlg = gui.DlgFromDict(runtime_vars, order=order, title=exp_title)
    #got this from assignment code
    if dlg.OK:
        return runtime_vars
    else: 
        print('User Cancelled')

runtime_vars = getRuntimeVariables(runtime_vars_template, order=order)

#generate trials
generate_trials(runtime_vars['subj_code'], runtime_vars['seed'], runtime_vars['num_reps'])

#read in trials
def import_trials(trial_filename, col_names=None, separator=','):
    trial_file = open(trial_filename, 'r')
    if col_names is None:
        # Assume the first row contains the column names
        col_names = trial_file.readline().rstrip().split(separator)
    trials_list = []
    #loop through each line in trial_file
    for cur_trial in trial_file:
        cur_trial = cur_trial.rstrip().split(separator)
        assert len(cur_trial) == len(col_names) # make sure the number of column names = number of columns
        #create a dict of pairwise values in col_names and cur_trial
        trial_dict = dict(zip(col_names, cur_trial))
        trials_list.append(trial_dict)
    return trials_list

trials_list = import_trials(f"trials/{runtime_vars['subj_code']}_trials.csv")

def make_incongruent(cur_color): 
    """Return a random color that is different from the color passed in. 
    :Parameters:
        cur_color : string
            Current color of the stimuli
    """
    #list comprehension solution from assignment code!
    #much better than my original solution, 
    #which is to randomly choosing from the full stimuli list in a while loop and hope for the best...
    incongruent_colors = [stim for stim in stimuli if stim != cur_color]
    return random.choice(incongruent_colors)

for cur_trial in trials_list:
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
        break

print(RTs)
win.close()
core.quit()
        
