START = '\033[' 
END = '\033[0m'
DEL = ';'
M = 'm'

class Color(object):

    def __init__(self, color_id=''):
        self.color_id = color_id
        if color_id:
            self.color_str = "%s%s%s" % (START, color_id, M)
        else:
            self.color_str = ""
       
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

        return ''.join([beginning, self.color_str, colored, END, end])
        #return '%s%s%s%s%s' % (beginning, self.color_str, colored, END, end)

    def __add__(self, other):
        return self.__repr__() + other

    def __repr__(self):
        return self.color_str

    def __str__(self):
        return str(self.color_id)

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
        self.color_str = "%s%s%s%s%s" % (START, effect, DEL, self.color_id, M)

class BG(object):
    """Effects are not supported for background colors
    """
    Black = Color(40)
    Red = Color(41)
    Green = Color(42)
    Brown = Color(43)
    Blue = Color(44)
    Purple = Color(45)
    Cyan = Color(46)
    Gray = Color(47)

class FG(object):
    """Foreground colors support effects, such as bolding and blinking,
    see C{EffectiveColor} for a description of all effects available.
    """
    Black = EffectiveColor(30)#bold = DarkGray
    Red = EffectiveColor(31)
    Green = EffectiveColor(32)
    Yellow = EffectiveColor(33)
    Blue = EffectiveColor(34)
    Purple = EffectiveColor(35)
    Cyan = EffectiveColor(36)
    Gray = EffectiveColor(37)#bold = White

