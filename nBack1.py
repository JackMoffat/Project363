from psychopy import visual, event, core
import pandas as pd
import random
import time as systime

#########
# setup #
#############################

#############
# Make lists / define functions #
#############



def makeMatches(in_list,n_trials_internal=5,
                threshold=0, n_back=2,
                keep_list_stats=True, verbose=False):
    '''Creates the matches in a given list.if a random number is greater than threshold,
    then match the letters at positions [idx] and [idx-n_back]
    in_list: list of letters, strings, etc
    threshold: type(float) in range(0,1)ld
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
match_frequency_threshold = 0.5 # need to think of this inverted with how the code is currently written
alphabet = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
initial_letters = [random.choice(alphabet) for i in range(n_trials)]

trial_list = makeMatches(initial_letters,n_trials,
                         threshold=match_frequency_threshold, keep_list_stats=False)
ptt = 1.2
# ptt is the amount of time between trials, stands for "per time trial"

######################
# Window setup below #
######################
mywin = visual.Window(fullscr=True, screen=0, allowGUI=False, allowStencil=False,
                      monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb')

clock = core.Clock()  # this is a clock

press_times = []  # List records the data


##############################

intro = False

if intro:
# TODO  Find out how to display the last sentence in text_string
    text_string = f"This is an N-Back task.  This task is a test of working memory.  You will be presented with a random series of letters, one by one.  For this task, you will press the spacebar if you see a letter that was repeated two letters back.  For example, if you see a sequence such as A, D, A, then you will have to press the spacebar.  You will be given a sequence of {n_trials} letters.  "
    textList = text_string.split("  ")
    for msg in textList:
        displayMsg = visual.TextStim(
            mywin, text = msg, pos=(0.5, 0))
        mywin.flip()
        displayMsg.draw()
        core.wait(3.5)
        countdownMessage = visual.TextStim(
            mywin, text='The task will begin after this countdown.', pos=(0.5, 0))
        countdownMessage.autoDraw = True
        mywin.flip()
        core.wait(3.5)
        countdowntxtDisplay.text = ' '
        mywin.flip()
        core.wait(2.0)



countdownString = "5,4,3,2,1"
countdown = countdownString.split(',')
# ct is the countdown timer

for num in countdown:
    txtDisplay = visual.TextStim(
	mywin, text = num , alignHoriz='left', alignVert='center', pos=(0, 0))
    mywin.flip()
    txtDisplay.draw()
    core.wait(1.0)
    

###################
# display letters #
###################


for idx, char in enumerate(trial_list):

    txtDisplay.text = char
    keys = event.getKeys(keyList=["space"], timeStamped=False)
    mywin.flip()
    txtDisplay.draw()
    print(keys, txtDisplay.text)
    press_times.append([keys, txtDisplay.text])
    core.wait(ptt)
    txtDisplay.text = "+"
    mywin.flip()
    txtDisplay.draw()
    core.wait(ptt)
    # currently appending in tuple form list_stats = []  # list holding the character and positions it was matched at

endMessage = visual.TextStim(
    mywin, text='You have completed the N-Back task. Thank you!', pos=(0.5, 0))
mywin.flip()
endMessage.autoDraw = True
core.wait(3.0)	

print(press_times)

# removed ptname, kept timestamp; timestamp is format Y(year)M(month)D(day)H(hour)M(minute)S(second)

ts = systime.localtime()
timestamp = str(systime.strftime("Y%yM%mD%dH%HM%MS%S",ts))
datafile = open(f"datafile_{timestamp}.txt", "w+")

################
# writing file #
################

# add datafile.write(trialconditions like time, n_trials, time per window, etc)


for line in press_times:
    datafile.write(str(line))
    datafile.write("\n")
datafile.close()

# #not sure needed
# for line in n_list:
#     datafile.write(line,)
#     datafile.write("\n")

0# for line in stats:
#     datafile.write(line)
#     datafile.write("\n")
