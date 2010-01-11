class Colors(object):
    def __init__(self):
        pass

    def disable(self):
        for x in self.__dict__.keys():
            self.x.disable()


	
START = '\033[' 
END = '\033[0m'

class Color(object):

    def __init__(self, color):
        self.color = color
        self.is_disabled = False
        self.color_str = START + color
       
    def disable(self):
        self.is_disabled = True

    def colorize(self, line, start_index=0, end_index=None):
        """If self.is_disabled then return line otherwise return colored line

        @param line
        @param start_index defaults to 0
        @param start_index defaults to len(line)
        """
        if self.is_disabled: return line
        if not end_index: end_index = len(line)

        beginning = line[:start_index]
        colored = line[start_index:end_index]
        end = line[end_index:]

        return '%s%s%s%s%s' % (beginning, self.color_str, colored, END, end)

    def __add__(self, other):
        return self.__repr__() + other

    def __repr__(self):
        return '' if self.is_disabled else self.color_str

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

