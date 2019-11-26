#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.78.01), June 24, 2014, at 15:49
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'N-Back_v.1'  # from the Builder filename that created this script
expInfo = {u'Test Session (1 or 2)': u'', u'Subject': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['Subject'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Administrator\\Desktop\\Robust_Tasks\\task_files\\N-Back_psychopy\\N-Back_v.1.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Setup the Window
win = visual.Window(size=(1024, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-0.15,-0.15,-0.15], colorSpace='rgb')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win._getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trigger"
triggerClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text="The program is ready, and will now start when triggered by the MR-scanner output pulse. (hit 't' to proceed manually, e.g. for demo purposes)",    font='Arial',
    pos=[0, -0.95], height=0.03, wrapWidth=2,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image_5 = visual.ImageStim(win=win, name='image_5',
    image='right_hand_nback.png', mask=None,
    ori=0, pos=[0, -0.3], size=[0.8, 1.2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=False, depth=-3.0)
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text="Buttons used in this task:\r\nIndex finger ('Yes')\r\nMiddle finger ('No')",    font='Arial',
    pos=[0, 0.6], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "selectBlock"
selectBlockClock = core.Clock()
nReps0Back=0
nReps2Back=0

# Initialize components for Routine "routine_0_Back_Target"
routine_0_Back_TargetClock = core.Clock()
Back0Target=[]
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='nonsense',    font='Arial',
    pos=[0, 0], height=0.4, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text = visual.TextStim(win=win, ori=0, name='text',
    text='TARGET',    font='Arial',
    pos=[0, 0.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "routine_0_Back"
routine_0_BackClock = core.Clock()
letter=[]

letterText = visual.TextStim(win=win, ori=0, name='letterText',
    text='nonsense',    font='Arial',
    pos=[0,0], height=0.4, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
promptText = visual.TextStim(win=win, ori=0, name='promptText',
    text='Matches Target?',    font='Arial',
    pos=[0, 0.5], height=0.2, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
image = visual.ImageStim(win=win, name='image',
    image='yes_key.jpg', mask=None,
    ori=0, pos=[-0.3, -0.7], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-3.0)
image_2 = visual.ImageStim(win=win, name='image_2',
    image='no_key.jpg', mask=None,
    ori=0, pos=[0.3, -0.7], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='Relax',    font='Arial',
    pos=[0, 0.5], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "routine_2_Back_Target"
routine_2_Back_TargetClock = core.Clock()
Back2minus1=[]
Back2minus2=[]
text3 = visual.TextStim(win=win, ori=0, name='text3',
    text='nonsense',    font='Arial',
    pos=[0, 0], height=0.4, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
Back2promptText = visual.TextStim(win=win, ori=0, name='Back2promptText',
    text='Matches 2 Back?',    font='Arial',
    pos=[0, 0.5], height=0.2, wrapWidth=2,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "routine_2_Back"
routine_2_BackClock = core.Clock()

text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='nonsense',    font='Arial',
    pos=[0,0], height=0.4, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
Back2Text = visual.TextStim(win=win, ori=0, name='Back2Text',
    text='Matches 2 Back?',    font='Arial',
    pos=[0, 0.5], height=0.2, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
image_3 = visual.ImageStim(win=win, name='image_3',
    image='yes_key.jpg', mask=None,
    ori=0, pos=[-0.3, -0.7], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-3.0)
image_4 = visual.ImageStim(win=win, name='image_4',
    image='no_key.jpg', mask=None,
    ori=0, pos=[0.3, -0.7], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='Relax',    font='Arial',
    pos=[0, 0.5], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "trigger"-------
t = 0
triggerClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
triggerComponents = []
triggerComponents.append(mouse)
triggerComponents.append(text_2)
triggerComponents.append(key_resp_4)
triggerComponents.append(image_5)
triggerComponents.append(text_6)
for thisComponent in triggerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trigger"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = triggerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *mouse* updates
    if t >= 0.0 and mouse.status == NOT_STARTED:
        # keep track of start time/frame for later
        mouse.tStart = t  # underestimates by a little under one frame
        mouse.frameNStart = frameN  # exact frame index
        mouse.status = STARTED
        event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
    if mouse.status == STARTED:  # only update if started and not stopped!
        buttons = mouse.getPressed()
        if sum(buttons) > 0:  # ie if any button is pressed
            # abort routine on response
            continueRoutine = False
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['t'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_5* updates
    if t >= 0.0 and image_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_5.tStart = t  # underestimates by a little under one frame
        image_5.frameNStart = frameN  # exact frame index
        image_5.setAutoDraw(True)
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "trigger"-------
for thisComponent in triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
BlocksLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath='C:\\Users\\Administrator\\Desktop\\Robust_Tasks\\task_files\\N-Back_psychopy\\N-Back_v.1.psyexp',
    trialList=data.importConditions('blocks_loop.xlsx'),
    seed=None, name='BlocksLoop')
thisExp.addLoop(BlocksLoop)  # add the loop to the experiment
thisBlocksLoop = BlocksLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlocksLoop.rgb)
if thisBlocksLoop != None:
    for paramName in thisBlocksLoop.keys():
        exec(paramName + '= thisBlocksLoop.' + paramName)

for thisBlocksLoop in BlocksLoop:
    currentLoop = BlocksLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBlocksLoop.rgb)
    if thisBlocksLoop != None:
        for paramName in thisBlocksLoop.keys():
            exec(paramName + '= thisBlocksLoop.' + paramName)
    
    #------Prepare to start Routine "selectBlock"-------
    t = 0
    selectBlockClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if (BlockCode==1):
        nReps0Back=1
        nReps2Back=0
    elif (BlockCode==2):
        nReps0Back=0
        nReps2Back=1
    # keep track of which components have finished
    selectBlockComponents = []
    for thisComponent in selectBlockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "selectBlock"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = selectBlockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selectBlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "selectBlock"-------
    for thisComponent in selectBlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # set up handler to look after randomisation of conditions etc
    Back0Loop = data.TrialHandler(nReps=nReps0Back, method='random', 
        extraInfo=expInfo, originPath='C:\\Users\\Administrator\\Desktop\\Robust_Tasks\\task_files\\N-Back_psychopy\\N-Back_v.1.psyexp',
        trialList=[None],
        seed=None, name='Back0Loop')
    thisExp.addLoop(Back0Loop)  # add the loop to the experiment
    thisBack0Loop = Back0Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisBack0Loop.rgb)
    if thisBack0Loop != None:
        for paramName in thisBack0Loop.keys():
            exec(paramName + '= thisBack0Loop.' + paramName)
    
    for thisBack0Loop in Back0Loop:
        currentLoop = Back0Loop
        # abbreviate parameter names if possible (e.g. rgb = thisBack0Loop.rgb)
        if thisBack0Loop != None:
            for paramName in thisBack0Loop.keys():
                exec(paramName + '= thisBack0Loop.' + paramName)
        
        #------Prepare to start Routine "routine_0_Back_Target"-------
        t = 0
        routine_0_Back_TargetClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        
        letters = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
        from random import choice
        Back0Target=choice(letters)
        text_3.setText(Back0Target)
        # keep track of which components have finished
        routine_0_Back_TargetComponents = []
        routine_0_Back_TargetComponents.append(text_3)
        routine_0_Back_TargetComponents.append(text)
        for thisComponent in routine_0_Back_TargetComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "routine_0_Back_Target"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = routine_0_Back_TargetClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_3* updates
            if t >= 0.0 and text_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_3.tStart = t  # underestimates by a little under one frame
                text_3.frameNStart = frameN  # exact frame index
                text_3.setAutoDraw(True)
            elif text_3.status == STARTED and t >= (0.0 + 2):
                text_3.setAutoDraw(False)
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t  # underestimates by a little under one frame
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            elif text.status == STARTED and t >= (0.0 + 2):
                text.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_0_Back_TargetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "routine_0_Back_Target"-------
        for thisComponent in routine_0_Back_TargetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # set up handler to look after randomisation of conditions etc
        Back0TrialsLoop = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath='C:\\Users\\Administrator\\Desktop\\Robust_Tasks\\task_files\\N-Back_psychopy\\N-Back_v.1.psyexp',
            trialList=data.importConditions('0-back_loop.xlsx'),
            seed=None, name='Back0TrialsLoop')
        thisExp.addLoop(Back0TrialsLoop)  # add the loop to the experiment
        thisBack0TrialsLoop = Back0TrialsLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisBack0TrialsLoop.rgb)
        if thisBack0TrialsLoop != None:
            for paramName in thisBack0TrialsLoop.keys():
                exec(paramName + '= thisBack0TrialsLoop.' + paramName)
        
        for thisBack0TrialsLoop in Back0TrialsLoop:
            currentLoop = Back0TrialsLoop
            # abbreviate parameter names if possible (e.g. rgb = thisBack0TrialsLoop.rgb)
            if thisBack0TrialsLoop != None:
                for paramName in thisBack0TrialsLoop.keys():
                    exec(paramName + '= thisBack0TrialsLoop.' + paramName)
            
            #------Prepare to start Routine "routine_0_Back"-------
            t = 0
            routine_0_BackClock.reset()  # clock 
            frameN = -1
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            if trialType=='nonTarget':
                letters = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
                from random import choice
                letter=choice(letters)
            elif trialType=='target':
                letter=Back0Target 
            
            letterText.setText(letter)
            key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
            key_resp_2.status = NOT_STARTED
            # keep track of which components have finished
            routine_0_BackComponents = []
            routine_0_BackComponents.append(letterText)
            routine_0_BackComponents.append(promptText)
            routine_0_BackComponents.append(image)
            routine_0_BackComponents.append(image_2)
            routine_0_BackComponents.append(key_resp_2)
            for thisComponent in routine_0_BackComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "routine_0_Back"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = routine_0_BackClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if len(key_resp_2.keys)==0:
                    letterXpos=0
                if len(key_resp_2.keys)>0:
                    letterXpos=2
                
                # *letterText* updates
                if t >= 0.0 and letterText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    letterText.tStart = t  # underestimates by a little under one frame
                    letterText.frameNStart = frameN  # exact frame index
                    letterText.setAutoDraw(True)
                elif letterText.status == STARTED and t >= (0.0 + 2):
                    letterText.setAutoDraw(False)
                if letterText.status == STARTED:  # only update if being drawn
                    letterText.setPos([letterXpos, 0], log=False)
                
                # *promptText* updates
                if t >= 0.0 and promptText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    promptText.tStart = t  # underestimates by a little under one frame
                    promptText.frameNStart = frameN  # exact frame index
                    promptText.setAutoDraw(True)
                elif promptText.status == STARTED and t >= (0.0 + 2):
                    promptText.setAutoDraw(False)
                
                # *image* updates
                if t >= 0.0 and image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image.tStart = t  # underestimates by a little under one frame
                    image.frameNStart = frameN  # exact frame index
                    image.setAutoDraw(True)
                elif image.status == STARTED and t >= (0.0 + 2):
                    image.setAutoDraw(False)
                
                # *image_2* updates
                if t >= 0.0 and image_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_2.tStart = t  # underestimates by a little under one frame
                    image_2.frameNStart = frameN  # exact frame index
                    image_2.setAutoDraw(True)
                elif image_2.status == STARTED and t >= (0.0 + 2):
                    image_2.setAutoDraw(False)
                
                # *key_resp_2* updates
                if t >= 0.0 and key_resp_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_2.tStart = t  # underestimates by a little under one frame
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    key_resp_2.clock.reset()  # now t=0
                    event.clearEvents()
                elif key_resp_2.status == STARTED and t >= (0.0 + 2):
                    key_resp_2.status = STOPPED
                if key_resp_2.status == STARTED:
                    theseKeys = event.getKeys(keyList=['2', '3', '4'])
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if key_resp_2.keys == []:  # then this was the first keypress
                            key_resp_2.keys = theseKeys[0]  # just the first key pressed
                            key_resp_2.rt = key_resp_2.clock.getTime()
                            # was this 'correct'?
                            if (key_resp_2.keys == str(corrResponse)): key_resp_2.corr = 1
                            else: key_resp_2.corr=0
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in routine_0_BackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "routine_0_Back"-------
            for thisComponent in routine_0_BackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            letterXpos=0
            # check responses
            if len(key_resp_2.keys) == 0:  # No response was made
               key_resp_2.keys=None
               # was no response the correct answer?!
               if str(corrResponse).lower() == 'none': key_resp_2.corr = 1  # correct non-response
               else: key_resp_2.corr = 0  # failed to respond (incorrectly)
            # store data for Back0TrialsLoop (TrialHandler)
            Back0TrialsLoop.addData('key_resp_2.keys',key_resp_2.keys)
            Back0TrialsLoop.addData('key_resp_2.corr', key_resp_2.corr)
            if key_resp_2.keys != None:  # we had a response
                Back0TrialsLoop.addData('key_resp_2.rt', key_resp_2.rt)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'Back0TrialsLoop'
        
        
        #------Prepare to start Routine "rest"-------
        t = 0
        restClock.reset()  # clock 
        frameN = -1
        routineTimer.add(9.990000)
        # update component parameters for each repeat
        # keep track of which components have finished
        restComponents = []
        restComponents.append(text_5)
        for thisComponent in restComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "rest"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = restClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if t >= 0.0 and text_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_5.tStart = t  # underestimates by a little under one frame
                text_5.frameNStart = frameN  # exact frame index
                text_5.setAutoDraw(True)
            elif text_5.status == STARTED and t >= (0.0 + 9.99):
                text_5.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in restComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "rest"-------
        for thisComponent in restComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed nReps0Back repeats of 'Back0Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    Back2Loop = data.TrialHandler(nReps=nReps2Back, method='random', 
        extraInfo=expInfo, originPath='C:\\Users\\Administrator\\Desktop\\Robust_Tasks\\task_files\\N-Back_psychopy\\N-Back_v.1.psyexp',
        trialList=[None],
        seed=None, name='Back2Loop')
    thisExp.addLoop(Back2Loop)  # add the loop to the experiment
    thisBack2Loop = Back2Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisBack2Loop.rgb)
    if thisBack2Loop != None:
        for paramName in thisBack2Loop.keys():
            exec(paramName + '= thisBack2Loop.' + paramName)
    
    for thisBack2Loop in Back2Loop:
        currentLoop = Back2Loop
        # abbreviate parameter names if possible (e.g. rgb = thisBack2Loop.rgb)
        if thisBack2Loop != None:
            for paramName in thisBack2Loop.keys():
                exec(paramName + '= thisBack2Loop.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        Back2TargetLoop = data.TrialHandler(nReps=2, method='random', 
            extraInfo=expInfo, originPath='C:\\Users\\Administrator\\Desktop\\Robust_Tasks\\task_files\\N-Back_psychopy\\N-Back_v.1.psyexp',
            trialList=[None],
            seed=None, name='Back2TargetLoop')
        thisExp.addLoop(Back2TargetLoop)  # add the loop to the experiment
        thisBack2TargetLoop = Back2TargetLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisBack2TargetLoop.rgb)
        if thisBack2TargetLoop != None:
            for paramName in thisBack2TargetLoop.keys():
                exec(paramName + '= thisBack2TargetLoop.' + paramName)
        
        for thisBack2TargetLoop in Back2TargetLoop:
            currentLoop = Back2TargetLoop
            # abbreviate parameter names if possible (e.g. rgb = thisBack2TargetLoop.rgb)
            if thisBack2TargetLoop != None:
                for paramName in thisBack2TargetLoop.keys():
                    exec(paramName + '= thisBack2TargetLoop.' + paramName)
            
            #------Prepare to start Routine "routine_2_Back_Target"-------
            t = 0
            routine_2_Back_TargetClock.reset()  # clock 
            frameN = -1
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            letters = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
            from random import choice
            letter=choice(letters)
            
            text3.setText(letter)
            # keep track of which components have finished
            routine_2_Back_TargetComponents = []
            routine_2_Back_TargetComponents.append(text3)
            routine_2_Back_TargetComponents.append(Back2promptText)
            for thisComponent in routine_2_Back_TargetComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "routine_2_Back_Target"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = routine_2_Back_TargetClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *text3* updates
                if t >= 0.0 and text3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text3.tStart = t  # underestimates by a little under one frame
                    text3.frameNStart = frameN  # exact frame index
                    text3.setAutoDraw(True)
                elif text3.status == STARTED and t >= (0.0 + 2):
                    text3.setAutoDraw(False)
                
                # *Back2promptText* updates
                if t >= 0.0 and Back2promptText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Back2promptText.tStart = t  # underestimates by a little under one frame
                    Back2promptText.frameNStart = frameN  # exact frame index
                    Back2promptText.setAutoDraw(True)
                elif Back2promptText.status == STARTED and t >= (0.0 + 2):
                    Back2promptText.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in routine_2_Back_TargetComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "routine_2_Back_Target"-------
            for thisComponent in routine_2_Back_TargetComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Back2minus2=Back2minus1
            Back2minus1=letter
            thisExp.nextEntry()
            
        # completed 2 repeats of 'Back2TargetLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        Back2TrialsLoop = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath='C:\\Users\\Administrator\\Desktop\\Robust_Tasks\\task_files\\N-Back_psychopy\\N-Back_v.1.psyexp',
            trialList=data.importConditions('2-back_loop.xlsx'),
            seed=None, name='Back2TrialsLoop')
        thisExp.addLoop(Back2TrialsLoop)  # add the loop to the experiment
        thisBack2TrialsLoop = Back2TrialsLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisBack2TrialsLoop.rgb)
        if thisBack2TrialsLoop != None:
            for paramName in thisBack2TrialsLoop.keys():
                exec(paramName + '= thisBack2TrialsLoop.' + paramName)
        
        for thisBack2TrialsLoop in Back2TrialsLoop:
            currentLoop = Back2TrialsLoop
            # abbreviate parameter names if possible (e.g. rgb = thisBack2TrialsLoop.rgb)
            if thisBack2TrialsLoop != None:
                for paramName in thisBack2TrialsLoop.keys():
                    exec(paramName + '= thisBack2TrialsLoop.' + paramName)
            
            #------Prepare to start Routine "routine_2_Back"-------
            t = 0
            routine_2_BackClock.reset()  # clock 
            frameN = -1
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            if trialType=='nonTarget':
                letters = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
                from random import choice
                letter=choice(letters)
                if letter==Back2minus1:
                        from random import choice
                        letter=choice(letters)
            elif trialType=='target':
                letter=Back2minus2
            text_4.setText(letter)
            key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
            key_resp_3.status = NOT_STARTED
            # keep track of which components have finished
            routine_2_BackComponents = []
            routine_2_BackComponents.append(text_4)
            routine_2_BackComponents.append(Back2Text)
            routine_2_BackComponents.append(image_3)
            routine_2_BackComponents.append(image_4)
            routine_2_BackComponents.append(key_resp_3)
            for thisComponent in routine_2_BackComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "routine_2_Back"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = routine_2_BackClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if len(key_resp_3.keys)==0:
                    letterXpos=0
                if len(key_resp_3.keys)>0:
                    letterXpos=2
                
                # *text_4* updates
                if t >= 0.0 and text_4.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_4.tStart = t  # underestimates by a little under one frame
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.setAutoDraw(True)
                elif text_4.status == STARTED and t >= (0.0 + 2):
                    text_4.setAutoDraw(False)
                if text_4.status == STARTED:  # only update if being drawn
                    text_4.setPos([letterXpos, 0], log=False)
                
                # *Back2Text* updates
                if t >= 0.0 and Back2Text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Back2Text.tStart = t  # underestimates by a little under one frame
                    Back2Text.frameNStart = frameN  # exact frame index
                    Back2Text.setAutoDraw(True)
                elif Back2Text.status == STARTED and t >= (0.0 + 2):
                    Back2Text.setAutoDraw(False)
                
                # *image_3* updates
                if t >= 0.0 and image_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_3.tStart = t  # underestimates by a little under one frame
                    image_3.frameNStart = frameN  # exact frame index
                    image_3.setAutoDraw(True)
                elif image_3.status == STARTED and t >= (0.0 + 2):
                    image_3.setAutoDraw(False)
                
                # *image_4* updates
                if t >= 0.0 and image_4.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_4.tStart = t  # underestimates by a little under one frame
                    image_4.frameNStart = frameN  # exact frame index
                    image_4.setAutoDraw(True)
                elif image_4.status == STARTED and t >= (0.0 + 2):
                    image_4.setAutoDraw(False)
                
                # *key_resp_3* updates
                if t >= 0.0 and key_resp_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_3.tStart = t  # underestimates by a little under one frame
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    key_resp_3.clock.reset()  # now t=0
                    event.clearEvents()
                elif key_resp_3.status == STARTED and t >= (0.0 + 2):
                    key_resp_3.status = STOPPED
                if key_resp_3.status == STARTED:
                    theseKeys = event.getKeys(keyList=['2', '3', '4'])
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                        key_resp_3.rt = key_resp_3.clock.getTime()
                        # was this 'correct'?
                        if (key_resp_3.keys == str(corrResponse)): key_resp_3.corr = 1
                        else: key_resp_3.corr=0
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in routine_2_BackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "routine_2_Back"-------
            for thisComponent in routine_2_BackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Back2minus2=Back2minus1
            Back2minus1=letter
            letterXpos=0
            # check responses
            if len(key_resp_3.keys) == 0:  # No response was made
               key_resp_3.keys=None
               # was no response the correct answer?!
               if str(corrResponse).lower() == 'none': key_resp_3.corr = 1  # correct non-response
               else: key_resp_3.corr = 0  # failed to respond (incorrectly)
            # store data for Back2TrialsLoop (TrialHandler)
            Back2TrialsLoop.addData('key_resp_3.keys',key_resp_3.keys)
            Back2TrialsLoop.addData('key_resp_3.corr', key_resp_3.corr)
            if key_resp_3.keys != None:  # we had a response
                Back2TrialsLoop.addData('key_resp_3.rt', key_resp_3.rt)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'Back2TrialsLoop'
        
        
        #------Prepare to start Routine "rest"-------
        t = 0
        restClock.reset()  # clock 
        frameN = -1
        routineTimer.add(9.990000)
        # update component parameters for each repeat
        # keep track of which components have finished
        restComponents = []
        restComponents.append(text_5)
        for thisComponent in restComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "rest"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = restClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if t >= 0.0 and text_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_5.tStart = t  # underestimates by a little under one frame
                text_5.frameNStart = frameN  # exact frame index
                text_5.setAutoDraw(True)
            elif text_5.status == STARTED and t >= (0.0 + 9.99):
                text_5.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in restComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "rest"-------
        for thisComponent in restComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed nReps2Back repeats of 'Back2Loop'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'BlocksLoop'






win.close()
core.quit()
