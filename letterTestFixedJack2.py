from psychopy import visual, event, core
import pandas as pd
import random


#########
# setup #
#############################

#############
# functions #
#############
def makeMatches(in_list, n_back=2, threshold=0, keep_list_stats=True, verbose=False):
    '''Creates the matches in a given list.if a random number is greater than threshold,
    then match the letters at positions [idx] and [idx-n_back]
    in_list: list of letters, strings, etc
    threshold: type(float) in range(0,1)
    keep_stats: Bool: will output a list with information on
    the matches (position, character) and their frequency
verbose: Bool: prints information about the lists for immediate viewing
    '''

    # done this way to avoid changing original list, confirm necessity?
    out_list = [i for i in in_list]
    list_stats = []  # list holding the character and positions it was matched at
    num_matches = 0
    for idx, char in enumerate(in_list):
        if idx > 1:
            if (random.random() > threshold):
                out_list[idx] = in_list[idx-n_back]
                list_stats.append([(idx, idx-2), char]
                                  ) if keep_list_stats else None
                num_matches += 1

    real_match_rate = num_matches / (len(in_list) - 2)
    # show _stats or not
    if verbose:  # switch this out of a print statement for final thing so it doesnt show up
        print(
            f"{num_matches} of {len(in_list)-2} possible matches: {real_match_rate* 100} %")
        print(f"in_list\n", in_list, "\nmatched list\n", out_list)
    else:
        pass

    if keep_list_stats:
        list_stats.insert(0, [(num_matches), "number of matches"])
        list_stats.insert(0, [(real_match_rate), "actual match rate"])
        return(out_list, list_stats)
    else:
        return(out_list)


#####################
# create trial list #
#####################
n_trials = 15
n_matching = 5
match_frequency = 0.5
alphabet = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]


initial_letters = [random.choice(alphabet) for i in range(n_trials)]
trial_list = makeMatches(
    initial_letters, threshold=match_frequency, keep_list_stats=False, verbose=True)


######################
# Window setup below #
######################
mywin = visual.Window(fullscr=True, screen=0, allowGUI=False, allowStencil=False,
                      monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb')

clock = core.Clock()  # this is a clock

press_times = []  # List records the data


##############################


# introduction message
# beginMessage = visual.TextStim(
#    mywin, text='This is an N-Back task.', pos=(0.5, 0))
# mywin.flip()
# beginMessage.draw()
# mywin.flip()
# core.wait(3.5)

# TODO  Find out how to display the last sentence in text_string
text_string = "This is an N-Back task.  This task is a test of working memory.  You will be presented with a random series of letters, one by one.  For this task, you will press the spacebar if you see a letter that was repeated two letters back.  For example, if you see a sequence such as A, D, A, then you will have to press the spacebar.  You will be given a sequence of fifteen letters.  "
textList = text_string.split("  ")
for msg in textList:
    displayMsg = visual.TextStim(
    mywin, text = msg, pos=(0.5, 0))
    mywin.flip()
    displayMsg.draw()
    core.wait(3.5)

# mywin.flip()
# core.wait(3.5)
# beginMessage.text = 'This task is a test of working memory.'
# mywin.flip()
# core.wait(3.5)
# beginMessage.text = 'You will be presented with a random series of letters, one by one.'
# mywin.flip()
# core.wait(3.5)
# beginMessage.text = 'For this task, you will press the spacebar if you see a letter othat was repeated two letters back.'
# mywin.flip()
# core.wait(3.5)
# beginMessage.text = 'For example, if you see a sequence such as A, D, A, then you will have to press the spacebar.'
# mywin.flip()
# core.wait(4.0)
# beginMessage.text = 'You will be given a sequence of fifteen letters.'
# mywin.flip()
# core.wait(3.5)
# beginMessage.text = 'Please press the key corresponding to the first letter of your name.'
# mywin.flip()
# core.wait(3.5)

# keys = event.waitKeys(keyList=[i for i in alphabet])
# print(keys)
countdownMessage = visual.TextStim(
    mywin, text='The task will begin after this countdown.', pos=(0.5, 0))
countdownMessage.autoDraw = True
mywin.flip()
core.wait(3.5)
countdownMessage.text = ' '
mywin.flip()
core.wait(2.0)

##################
# Countdown here #
##################
# we can redo this one too

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


###################
# display letters #
###################

for idx, char in enumerate(trial_list):

    message.text = char
    mywin.flip()
    core.wait(1.3)
    keys = event.getKeys(keyList=["space"], timeStamped=False)
    print(keys, message.text)
    press_times.append((keys, message.text))
    message.text = "+"
    mywin.flip()
    core.wait(1.3)
    # currently appending in tuple form list_stats = []  # list holding the character and positions it was matched at


# message.text='A'
# mywin.flip()
# core.wait(1.3)
# keys=event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text='A'
# mywin.flip()
# core.wait(1.3)
# keys=event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text='D'
# mywin.flip()
# core.wait(1.3)
# keys=event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text='F'
# mywin.flip()
# core.wait(1.3)
# keys=event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text='G'
# mywin.flip()
# core.wait(1.3)
# keys=event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text='F'
# mywin.flip()
# core.wait(1.3)
# keys=event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text='V'
# mywin.flip()
# core.wait(1.3)
# keys=event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text='T'
# mywin.flip()
# core.wait(1.3)
# keys=event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text='V'
# mywin.flip()
# core.wait(1.3)
# keys=event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text='P'
# Fmywin.flip()
# core.wait(1.3)
# keys=event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text='C'
# mywin.flip()
# core.wait(1.3)
# keys=event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text='J'
# mywin.flip()
# core.wait(1.3)
# keys=event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text='H'
# mywin.flip()
# core.wait(1.3)
# keys = event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text = 'J'
# mywin.flip()
# core.wait(1.3)
# keys = event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text = 'H'
# mywin.flip()
# core.wait(1.3)
# keys = event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text = 'O'
# mywin.flip()
# core.wait(1.3)
# keys = event.getKeys(keyList=["space"], timeStamped=True)
# print(keys, message.text)

# message.text = ' '
# mywin.flip()
# core.wait(1.0)

# letter sequence ends here

endMessage = visual.TextStim(
    mywin, text='You have completed the N-Back task. Thank you!', pos=(0.5, 0))
mywin.flip()
endMessage.autoDraw = True
core.wait(3.0)

print(press_times)


datafile = open(f"data_{ptname}.txt", "w+")
for line in press_times:
    datafile.write(line)
    datafile.write("\n")

# #not sure needed
# for line in n_list:
#     datafile.write(line,)
#     datafile.write("\n")

# for line in stats:
#     datafile.write(line)
#     datafile.write("\n")
