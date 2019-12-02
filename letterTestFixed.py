from psychopy import visual, event, core
import pandas as pd
import random

# Window setup below
mywin = visual.Window(fullscr=True, screen=0, allowGUI=False, allowStencil=False, monitor='testMonitor', color=[0,0,0], colorSpace='rgb')

# CLock & keys setup

clock = core.Clock()
keys = event.getKeys(keyList=["space"], timeStamped=True)


# introduction message
beginMessage = visual.TextStim(mywin, text='This is an N-Back task.', pos=(0.5, 0))
beginMessage.autoDraw = True
mywin.flip()
core.wait(3.5)
beginMessage.text = 'This task is a test of working memory.'
mywin.flip()
core.wait(3.5)
beginMessage.text = 'You will be presented with a random series of letters, one by one.'
mywin.flip()
core.wait(3.5)
beginMessage.text = 'The task requires you to press a key if you see a letter that was repeated two letters back.'
mywin.flip()
core.wait(3.5)
beginMessage.text = 'For example, if you see a sequence such as A, D, A, then you will have to press a key.'
mywin.flip()
core.wait(4.0)
beginMessage.text = 'You will be given a sequence of fifteen letters.'
mywin.flip()
core.wait(3.5)
beginMessage.text = 'The task will begin after this countdown.'
mywin.flip()
core.wait(3.5)
beginMessage.text = ' '
mywin.flip()
core.wait(2.0)

# Countdown
message = visual.TextStim(mywin, text='5', alignHoriz='left', alignVert='center', pos=(0, 0))
message.autoDraw = True
mywin.flip()
core.wait(1.0)
message.text = '4'
mywin.flip()
core.wait(1.0)
message.text = '3'
mywin.flip()
core.wait(1.0)
message.text = '2'
mywin.flip()
core.wait(1.0)
message.text = '1'
mywin.flip()
core.wait(1.0)

# letter sequence starts here
message.text = 'A'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'D'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'F'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'G'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'F'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'V'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'T'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'V'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'P'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'C'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'J'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'H'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'J'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'H'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = 'O'
mywin.flip()
core.wait(1.3)
keys = event.getKeys(keyList=["space"], timeStamped=True)
print(keys, message.text)
message.text = ' '
mywin.flip()
core.wait(1.0)
endMessage = visual.TextStim(mywin, text='You have completed the N-Back task. Thank you!', pos=(0.5, 0))
endMessage.autoDraw = True
mywin.flip()
core.wait(3.0)