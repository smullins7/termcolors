START = '\033[' 
END = '\033[0m'

class Color(object):

    def __init__(self, color):
        self.color = color
        self.color_str = START + color
       
    def colorize(self, line, start_index=0, end_index=None):
        """Return colored line from start_index to end_index

        @param line: the string to colorize
        @param start_index: defaults to 0
        @param end_index: defaults to None
        """
        if not end_index: end_index = len(line)

        beginning = line[:start_index]
        colored = line[start_index:end_index]
        end = line[end_index:]

        return '%s%s%s%s%s' % (beginning, self.color_str, colored, END, end)

    def __add__(self, other):
        return self.__repr__() + other

    def __repr__(self):
        return self.color_str

class EffectiveColor(Color):
    """EffectiveColor supports the following effects:
    bold
    faint 
    italic
    underscore
    blink
    blinkfast
    inverse
    concealed
    strikeout
    """

    bold = 1
    faint = 2
    italic = 3
    underscore = 4
    blink = 5
    blinkfast = 6
    inverse = 7
    concealed = 8
    strikeout = 9

    def toggle(self, effect):
        """Only one effect may be used at a time for a given string.

        @param effect: the int value of the effect to turn on
        """
        self.color_str = "%s%s%s" % (START, effect, self.color)

class BG(object):
    """Effects are not supported for background colors
    """
    Black = Color(';40m')
    Red = Color(';41m')
    Green = Color(';42m')
    Brown = Color(';43m')
    Blue = Color(';44m')
    Purple = Color(';45m')
    Cyan = Color(';46m')
    Gray = Color(';47m')

class FG(object):
    """Foreground colors support effects, such as bolding and blinking,
    see C{EffectiveColor} for a description of all effects available.
    """
    Black = EffectiveColor(';30m')#bold = DarkGray
    Red = EffectiveColor(';31m')
    Green = EffectiveColor(';32m')
    Yellow = EffectiveColor(';33m')
    Blue = EffectiveColor(';34m')
    Purple = EffectiveColor(';35m')
    Cyan = EffectiveColor(';36m')
    Gray = EffectiveColor(';37m')#bold = White

