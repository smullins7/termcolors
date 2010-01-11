#!/usr/bin/python

from configuration import Config
from wrapper import Wrapper

colors = ['red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'gray']
bg_colors = ['black', 'red', 'green', 'brown', 'blue', 'purple', 'cyan', 'gray']

def test():
    """Not really a unit test with assertions, this is just
    a simple script to print all possible combinations of
    foreground colors, effects, and background colors to be
    verified by eyeballing.
    """
    config = Config()
    config.add_startswith('black', 'black', bg='gray')
    for color in colors:
        config.add_startswith(color, color)

    for color in bg_colors:
        fg = 'gray'
        if color == 'gray':
            fg = 'black'
            
        config.add_startswith('background %s' % color, fg, 'bold', color)

    wrapper = Wrapper(config)
    wrapper.output('black test line')
    for color in colors:
        wrapper.output('%s test line' % color)

    for color in bg_colors:
        wrapper.output('background %s test line' % color)

    #todo: test effects

if __name__=="__main__":
    test()
