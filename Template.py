from psychopy import core, visual, event
from psychopy.hardware import keyboard
import pandas as pd
import csv
import psychopy.clock
import psychopy.event
import random
import os

win = visual.Window([800,600], fullscr=False, monitor="testMonitor")
myMouse = event.Mouse(visible=False)
finalTable=[['image','Species', 'RespTime','Answer', 'Correct']]

message1= visual.TextStim(win, pos=[0,+0.1],text='Enter the participant number:')
message1.draw()
win.flip()
answer = ''

def show_cross(time):
    cross = visual.TextStim(win, text='+')
    cross.draw()
    win.flip()
    core.wait(time)

def block():
    grating = psychopy.visual.TextStim(win=win, text ='T')
    # Draw the stimulus to the window. We always draw at the back buffer of the window.
    grating.draw()
    # Flip back buffer and front  buffer of the window.
    win.flip()
    # Pause 0.5 s, so you get a chance to see it!
    core.wait(0.5)
    show_cross(0.5)
    choice = random.shuffle([0, 1])
    
    stimClock = core.Clock()
    '''
        key = psychopy.event.getKeys(keyList =['2','3'], timeStamped = stimClock)
        if len(key)>0:
            ans=key[len(key) -1]

            Resp_Time=ans[1]
            x = ans[0]
            if x=='2':
                Answer="1"
                if random_list [i] == 1:
                    Right = "Correct"
                if random_list [i] == 0:
                    Right = "Incorrect"
        else:
            Answer = '0'
            Resp_Time = 0
            if random_list [i] == 1:
                Right = "Incorrect"
            if random_list [i] == 0:
                Right = "Correct"
        row=[question, species, Resp_Time, Answer,Right]
        finalTable.append(row)
        '''
    cross = visual.TextStim(win, text='+')
    # Draw the stimulus to the window. We always draw at the back buffer of the window.
    cross.draw()
    # Flip back buffer and front  buffer of the window.
    win.flip()
    core.wait(0.75)

thisResp=None
while thisResp==None:
    allKeys=event.waitKeys()
    for thisKey in allKeys:  
        if thisKey=='space':
            thisResp=1
        elif thisKey=='return':
            thisResp=1
        elif thisKey=='backspace':
            answer=answer[:-1]
            message1.draw()
            message2 = visual.TextStim(win, pos=[0,-0.1],text=answer)
            message2.draw()
            win.flip()
        else:
            answer += thisKey
            message1.draw()
            message2 = visual.TextStim(win, pos=[0,-0.1],text=answer)
            message2.draw()
            win.flip()

for i in range(8):
    block()


# filename = 'images_'+answer+'.csv'

"""
with open(filename, 'a+', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(finalTable)
"""
core.quit()
