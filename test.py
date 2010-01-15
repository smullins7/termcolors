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

def test_from_file():
    config = Config('rc')
    wrapper = Wrapper(config)
    wrapper.output('red on white changeset line')
    wrapper.output('foo cyan on blue test line')
    wrapper.output('bar blue underlined test line')

def test_effects():
    fx = ['bold', 'faint', 'italic', 'underscore', 'blink', 'blinkfast', 'inverse', 'concealed', 'strikeout']
    config = Config()
    for effect in fx:
        config.add_contains(effect, 'gray', effect, 'black')

    wrapper = Wrapper(config)
    for effect in fx:
        wrapper.output("this line should have the %s effect" % effect)
    
if __name__=="__main__":
    test()
    test_from_file()
    test_effects()
