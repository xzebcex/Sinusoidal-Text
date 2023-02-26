# program title

import math
import shutil
import sys
import time

# Get the size of the terminal windows
WIDTH, HEIGHT = shutil.get_terminal_size()

WIDTH -= 1

print('Press ctrl-c to quit.')
print('Enter the message you want to display? (Max', WIDTH // 2, 'characters.)')
while True:
    message = input('Enter your mesage here: ')
    if 1 < len(message) <= (WIDTH // 2):
        break
    print('Message must be 1 to', WIDTH // 2, 'characters long.')


step = 0.0  # The step determine how far into the waves are
# Wave goes from -10-.0 ro 1.0, so we need to change it by a multiplier
multiplier = (WIDTH - len(message)) / 2
try:
    while True:
        sin_of_step = math.sin(step)
        padding = ' ' * int((sin_of_step + 1) * multiplier)
        print(padding + message)
        time.sleep(0.1)
        step += 0.10
except:
    sys.exit()  # When ctrl-c is pressed, program end
