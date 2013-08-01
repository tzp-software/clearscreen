'''
    clearscreen.main.py

    command line stuff
'''
from clearscreen import clear_screen
import sys

def print_usage():
    print 'usage'
    sys.exit(0)

def main():
    pause = None
    message = None
    fake = False
    wait = False

    # valid arguments
    ARGS = ['-l','--length','-m','--message','-f','--fake-mode','-w','--wait-mode']
    if len(sys.argv) > 1: 
        if sys.argv[1] in ARGS:
                if '-l' in sys.argv or '--length' in sys.argv:
                    if len(sys.argv) < 3:
                        print_usage()
                    else:
                        try:
                            pause = sys.argv[sys.argv.index('-l')+1]
                        except ValueError:
                            pause = sys.argv[sys.argv.index('--length')+1]

                if '-m' in sys.argv or '--message' in sys.argv:
                    try:
                        message = sys.argv[sys.argv.index('-m')+1]
                    except ValueError:
                        message = sys.argv[sys.argv.index('--message')+1]

                     
                if '-f' in sys.argv or '--fake-mode' in sys.argv:
                    fake = True

                if '-w' in sys.argv or '--wait-mode' in sys.argv:
                    wait = True


        clear_screen(length=pause,message=message,waitmode=wait,fakemode=fake)
    print_usage()

