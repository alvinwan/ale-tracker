"""
Sample script for the Arcade Learning Environment's Python interface

Usage:
    main.py <rom_file> [options]

Options:
    --iters=N   Number of iterations to run [default: 5]
    --display   Display the game being played. Uses SDL.
    --user      Give user control over agent. Control using action_indices.

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
import numpy as np

from ale_python_interface import ALEInterface


def random_agent(ale, legal_actions):
    return random.choice(legal_actions)


def main():
    arguments = docopt.docopt(__doc__, version='ALE Demo Version 1.0')

    pygame.init()

    ale = ALEInterface()
    ale.setInt(b'random_seed', 123)
    ale.setBool(b'display_screen', arguments['--display'])
    ale.loadROM(str.encode(arguments['<rom_file>']))
    legal_actions = ale.getLegalActionSet()

    entries, episode_rewards = None, []
    for episode in range(int(arguments['--iters'])):
        episode_reward = 0
        while not ale.game_over():
            if arguments['--user']:
                action_index = input('Act (0-%d): ' % len(legal_actions))
                action = legal_actions[int(action_index)]
            else:
                action = random_agent(ale, legal_actions)
            reward = ale.act(action)
            entry = np.array((np.ravel(ale.getScreen()), action, reward))
            entries = np.vstack((entries, entry)) if entries is not None \
                      else entry
            episode_reward += reward
        print('Episode %d ended with reward %d.' % (episode, episode_reward))
        episode_rewards.append(episode_reward)
        ale.reset_game()

    print('Average reward:', sum(episode_rewards)/len(episode_rewards))
    logpath = 'logs/log-{name}-{time}.csv'.format(
        name=os.path.basename(arguments['<rom_file>']).replace('.bin', ''),
        time=time.time())
    np.savez_compressed(logpath, entries)
    print('Data saved to', logpath)


if __name__ == '__main__':
    main()
