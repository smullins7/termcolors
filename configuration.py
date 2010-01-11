from color import BG, EffectiveColor, FG
from collections import defaultdict

class Config(object):
    def __init__(self, file=None):
        self.formatting = defaultdict(dict)
        self.default = ('', '')

    def add_default(self, fg, effect=None, bg=None):
        background, foreground = create_color(fg, effect, bg)
        self.default = (background, foreground)

    def add_contains(self, target, fg, effect=None, bg=None):
        background, foreground = create_color(fg, effect, bg)
        self.formatting['contains'][target] = (background, foreground)

    def add_startswith(self, target, fg, effect=None, bg=None):
        background, foreground = create_color(fg, effect, bg)
        self.formatting['startswith'][target] = (background, foreground)

    def format(self, target):
        for key, value in self.formatting['contains'].iteritems():
            if target.count(key):
                background, foreground = value
                return background + foreground.colorize(target)

        for key, value in self.formatting['startswith'].iteritems():
            if target.startswith(key):
                background, foreground = value
                return background + foreground.colorize(target)

        background, foreground = self.default
        return background + foreground.colorize(target)

def create_color(fg, effect=None, bg=None):
    if hasattr(FG, fg.capitalize()):
        foreground = getattr(FG, fg.capitalize())
    else:
        #throw an exception or use a default?
        pass

    if effect and type(effect) is int:
        foreground.toggle(effect)
    elif effect and type(effect) is str:
        effect_code = getattr(EffectiveColor, effect)
        foreground.toggle(effect_code)

    background = ''
    if bg:
        background = getattr(BG, bg.capitalize())

    return (background, foreground)
