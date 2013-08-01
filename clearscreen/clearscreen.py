'''
    clearscreen.clearscreen.py
'''
import os
import time

def _press_enter_to_continue():  # secret worker behind waitmode
    x = raw_input('Press Enter To Continue...')

def _pause(secs):    # secret worker behind length
    time.sleep(float(secs))

def _clear_screen():    # secret worker behind clear_screen
    x = os.system('clear')

def clear_screen(length=None,message=None,waitmode=False,fakemode=False):
    '''
    clears users screen if no options used, else

    length = time before returning control to user after clearing screen(secs)
    message = message to print to screen after clearing
    waitmode = boolean value, if True pauses and waits for enter key to resume
    fakemode = boolean value, if True does everything specified by options 
               but does not clear the screen
    '''
    if not fakemode:
        _clear_screen()

    if message is not None:
        print ('\n'*3) + message + ('\n'*2)

    if length is not None:
        _pause(length)

    if waitmode:
        _press_enter_to_continue()


if __name__ == "__main__":
    _clear_screen()



