import psychopy.visual
import psychopy.event
import psychopy.core

win = psychopy.visual.Window(
    fullscr=True,
    units="pix",
)

keys_times = []
clock = psychopy.core.Clock()
keys = psychopy.event.waitKeys(timeStamped=clock)


nTrials = 4
displayTime = 1.3
keys = []  # intialize keys

mywin = psychopy.visual.Window(fullscr=True, screen=0, allowGUI=True,
                               allowStencil=False, monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb')

message = psychopy.visual.TextStim(
    mywin, text="t", alignHoriz='left', alignVert='center', pos=(0, 0))
message.autoDraw = True
# initiating loop is issue right now

for i in range(nTrials):
    trialClock = psychopy.core.Clock()
    keys = psychopy.event.waitKeys(timeStamped=trialClock)
    psychopy.core.wait(displayTime)
    mywin.flip()
    # while len(keys) == 0:  # and trialClock < displayTime:
    #   trialClock = psychopy.core.Clock()


print(keys)


win.close()

[('left', 0.5030858516693115)]
