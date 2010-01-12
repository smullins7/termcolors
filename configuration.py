from color import BG, Color, EffectiveColor, FG
from collections import defaultdict

class Config(object):
    def __init__(self, file=None):
        self.formatting = defaultdict(dict)
        self.default = (Color(), Color())
        self.disabled = False

        if file:
            self.add_from_file(file)

    def disable(self):
        self.disabled = True

    def add_default(self, fg=None, effect=None, bg=None):
        background, foreground = create_color(fg, effect, bg)
        self.default = (background, foreground)

    def add_contains(self, target, fg=None, effect=None, bg=None):
        background, foreground = create_color(fg, effect, bg)
        self.formatting['contains'][target] = (background, foreground)

    def add_startswith(self, target, fg=None, effect=None, bg=None):
        background, foreground = create_color(fg, effect, bg)
        self.formatting['startswith'][target] = (background, foreground)

    def format(self, target):
        if self.disabled:
            return target

        for key, value in self.formatting['contains'].iteritems():
            if target.count(key):
                background, foreground = value
                return background + foreground.colorize(target)

        for key, value in self.formatting['startswith'].iteritems():
            if target.startswith(key):
                background, foreground = value
                return background + foreground.colorize(target)

        background, foreground = self.default
        return "%s%s" % (background, foreground.colorize(target))

    def add_from_file(self, file_name):
        for line in open(file_name):
            line = line.strip()
            fields = line.split(' ')
            if len(fields) < 2:
                continue

            type = fields.pop(0)
            if type != 'default':
                target = fields.pop(0)
            fg = None
            bg = None
            effect = None
            for param_str in fields:
                key, value = tuple(param_str.split('='))
                if key == 'fg':
                    fg = value
                elif key == 'bg':
                    bg = value
                elif key == 'effect':
                    effect = value
            if type == 'contains':
                self.add_contains(target, fg, effect, bg)
            elif type == 'startswith':
                self.add_startswith(target, fg, effect, bg)
            elif type == 'default':
                self.add_default(fg, effect, bg)


def create_color(fg=None, effect=None, bg=None):
    foreground = Color()
    if fg and type(fg) is str and hasattr(FG, fg.capitalize()):
        foreground = getattr(FG, fg.capitalize())
    elif type(fg) is int:
        foreground = Color(fg)
    else:
        #throw an exception or use a default?
        pass

    if effect and type(effect) is int:
        foreground.toggle(effect)
    elif effect and type(effect) is str:
        effect_code = getattr(EffectiveColor, effect)
        foreground.toggle(effect_code)
    else:
        pass


    background = Color()
    if bg and type(bg) is str and hasattr(BG, bg.capitalize()):
        background = getattr(BG, bg.capitalize())
    elif type(bg) is int:
        background = Color(bg)
    else:
        #throw an exception or use a default?
        pass

    return (background, foreground)
