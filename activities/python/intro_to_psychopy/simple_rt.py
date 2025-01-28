from psychopy import visual, event, core # import the bits of PsychoPy we'll need for this walkthrough

#open a window
win = visual.Window([600,600],color="grey", units='pix', checkTiming=False) 

#create a circle
circle = visual.Circle(win,lineColor="grey",fillColor="blue", size=[100,100])

# create a list of colors
color_list = ['blue', 'orange', 'purple', 'red']

#create the instruction text
instruction_text = "Press b if the circle is blue and o if the circle is orange."
instruction = visual.TextStim(win, text = instruction_text,color="black", pos = (0,-100))

for current_color in color_list: 
    circle.color = current_color
    circle.draw()
    #draw the instruction
    instruction.draw()
    win.flip()
    
    key_pressed = event.waitKeys(keyList=['b', 'o', 'r', 'p'])
    if key_pressed: 
        print(key_pressed)
        win.flip()
    
    core.wait(1.0)

win.close() #close the window
core.quit() #quit out of the program

