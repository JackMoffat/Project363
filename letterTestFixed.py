from psychopy import visual, core
import pandas as pd
import random
mywin = visual.Window(size=(1920,1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False, monitor='testMonitor', color=[0,0,0], colorSpace='rgb')
letterStims = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
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
beginMessage.text = 'You will be given a sequence of ten letters.'
mywin.flip()
core.wait(3.5)
beginMessage.text = 'The task will begin after this countdown.'
mywin.flip()
core.wait(3.5)
beginMessage.text = ' '
mywin.flip()
core.wait(2.0)
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
# First letter
message.text = 'A'
mywin.flip()
core.wait(1.2)
message.text = 'D'
mywin.flip()
core.wait(1.2)
message.text = 'F'
mywin.flip()
core.wait(1.2)
message.text = 'G'
mywin.flip()
core.wait(1.2)
message.text = 'F'
mywin.flip()
core.wait(1.2)
message.text = 'V'
mywin.flip()
core.wait(1.2)
message.text = 'T'
mywin.flip()
core.wait(1.2)
message.text = 'V'
mywin.flip()
core.wait(1.2)
message.text = 'P'
mywin.flip()
core.wait(1.2)
message.text = 'C'
mywin.flip()
core.wait(1.2)
message.text = 'C'
mywin.flip()
core.wait(1.2)
message.text = 'H'
mywin.flip()
core.wait(1.2)
message.text = 'J'
mywin.flip()
core.wait(1.2)
message.text = 'H'
mywin.flip()
core.wait(1.2)
message.text = 'O'
mywin.flip()
core.wait(1.2)
message.text = ' '
mywin.flip()
core.wait(1.0)
endMessage = visual.TextStim(mywin, text='You have completed the N-Back task. Thank you!', pos=(0.5, 0))
endMessage.autoDraw = True
mywin.flip()
core.wait(3.0)