import time
import sys
from psychopy import visual,event,core # import the bits of PsychoPy we'll need for this exercise

#color_list = ['blue', 'red', 'blue', 'red', 'blue', 'red']
win = visual.Window([600,600],color="black", units='pix',checkTiming=False) #open a window
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100], 
                     pos=(-150, 0)) #create a Rectangle type object with certain parameters

blueSquare = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100], 
                         pos=(150,0))

# for color in color_list:
#     square.setFillColor(color)
#     square.draw()
#     win.flip()
#     core.wait(1)
#     win.flip()
#     core.wait(0.5)

square.draw()
blueSquare.draw()
win.flip()

ORI_STEP = 10
FULL_CIRCLE = 360
spin = True

# red square stuff
while(True):
    if (spin):
        square.setOri(square.ori + ORI_STEP)
        blueSquare.setOri(blueSquare.ori - ORI_STEP)
        square.draw()
        blueSquare.draw()
        win.flip()
        core.wait(1/(FULL_CIRCLE/ORI_STEP))
    if(event.getKeys(['q'])):
        break
    elif (event.getKeys(keyList = ['s'])):
        spin = False
    elif (event.getKeys(keyList = ['r'])):
        spin = True

# blue square stuff
while True:
    if(event.getKeys('left')):
        blueSquare.size += [-10, 0]
        blueSquare.draw()
        win.flip()
    elif(event.getKeys('right')):
        blueSquare.size += [10, 0]
        blueSquare.draw()
        win.flip()
    if(event.getKeys('q')):
        break

win.close() #close the window -- don't need this if you're running this as a separate file
core.quit() #quit out of the program -- don't need this if you're running this as a separate file