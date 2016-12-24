"""
Sample script for the Arcade Learning Environment's Python interface

Usage:
    demo.py <rom_file> [options]

Options:
    --iters=N    Number of iterations to run [default: 5]
    --display    Display the game being played. Uses SDL.

@author: Alvin Wan
@site: alvinwan.com
"""

import csv
import docopt
import random
import pygame
import os
import sys
import time

from ale_python_interface import ALEInterface


def main():
    arguments = docopt.docopt(__doc__, version='ALE Demo Version 1.0')

    pygame.init()

    ale = ALEInterface()
    ale.setInt(b'random_seed', 123)
    ale.setBool(b'display_screen', arguments['--display'])
    ale.loadROM(str.encode(arguments['<rom_file>']))
    legal_actions = ale.getLegalActionSet()

    logpath = 'logs/log-{name}-{time}.csv'.format(
        name=os.path.basename(arguments['<rom_file>']).replace('.bin', ''),
        time=time.time())
    with open(logpath, 'w') as f:
        rewards, writer = [], csv.writer(f)
        for episode in range(int(arguments['--iters'])):
            total_reward = 0
            while not ale.game_over():
                total_reward += ale.act(random.choice(legal_actions))
            print('Episode %d ended with reward %d.' % (episode, total_reward))
            rewards.append(total_reward)
            writer.writerow([total_reward])
            ale.reset_game()

    print('Average reward:', sum(rewards)/len(rewards))


if __name__ == '__main__':
    main()
