from psychopy import visual, core, data, event, gui
from psychopy.tools.filetools import fromFile, toFile
import numpy as np
import random


# ---- Data Collection

pt_name = ""

expInfo = {'observer': 'jwp', 'presstime': 0}

expInfo['dateStr'] = data.getDateStr()

dlg = gui.DlgFromDict(expInfo, title='N-back test', fixed=['dateStr'])
if dlg.OK:
    toFile(f"{pt_name}", expInfo)
else:
    core.quit()


filename = expInfo['observer'] + expInfo['dateStr']

dataFile = open(fileName+'.csv', 'w')  # may need to be w+
dataFile.write('noidea,fixthis\n')

globalTime = core.Clock()  # option 2
trialTime = core.Clock()


event.getKeys(timeStamped=True)


#----Window Setup ----#
mywin = visual.Window(fullscr=True, screen=0, allowGUI=True,
                      allowStencil=False, monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb')
letterStims = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
beginMessage = visual.TextStim(
    mywin, text='This is an N-Back task.', pos=(0.5, 0))
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


#---- Countdown ----#
beginMessage.text = 'The task will begin after this countdown.'
mywin.flip()
core.wait(3.5)
beginMessage.text = ' '
mywin.flip()
core.wait(2.0)
message = visual.TextStim(
    mywin, text='5', alignHoriz='left', alignVert='center', pos=(0, 0))
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


# ---- First letter

# Here is where we would want the recording
# We can make this a generator
keys = event.getKeys()

message.text = random.choice(letterStims)
mywin.flip()
core.wait(1.3)
message.text = random.choice(letterStims)
mywin.flip()
core.wait(1.3)
message.text = random.choice(letterStims)
mywin.flip()
core.wait(1.3)
message.text = random.choice(letterStims)
mywin.flip()
core.wait(1.3)
message.text = random.choice(letterStims)
mywin.flip()
core.wait(1.3)
message.text = random.choice(letterStims)
mywin.flip()
core.wait(1.3)
message.text = random.choice(letterStims)
mywin.flip()
core.wait(1.3)
message.text = random.choice(letterStims)
mywin.flip()
core.wait(1.3)
message.text = random.choice(letterStims)
mywin.flip()
core.wait(1.3)
message.text = random.choice(letterStims)
mywin.flip()
core.wait(1.3)
message.text = ' '
mywin.flip()
core.wait(1.3)
endMessage = visual.TextStim(
    mywin, text='Thank you for completing our N-Back task!', pos=(0.5, 0))
endMessage.autoDraw = True
mywin.flip()
core.wait(3.0)


# ---- writing participant output


write_output = csv.writer(open(f"{pt_name}.csv", "w+"), lineterminator='\n')
for i in range(0, len(responses)):
    write_output.writerow(responses[i])


#---- exit

if 'escape' in keys:
    core.quit()


# https://discourse.psychopy.org/t/record-keypress-and-time/953/2
