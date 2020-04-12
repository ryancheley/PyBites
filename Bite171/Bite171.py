from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    state = cycle(SPINNER_STATES)
    t_end = time() + seconds
    while time() < t_end:
        print(next(state), flush=True, end='\r')
        sys.stdout.flush()
        sleep(STATE_TRANSITION_TIME)

        # for i in state:
        #     print(i)
        #     print(time(), t_end)
        #     sleep(STATE_TRANSITION_TIME)


if __name__ == '__main__':
    spinner(2)