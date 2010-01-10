class Colors(object):
    def __init__(self):
        self.ENDC = Color('0m')
        self.Red = Color(';31m')
        self.Green = Color(';32m')
        self.Yellow = Color(';33m')
        self.Blue = Color(';34m')
        self.Purple = Color(';35m')
        self.Cyan = Color(';36m')
        self.Black = Color(';30m')#bold = DarkGray
        self.Gray = Color(';37m')#bold = White

    def disable(self):
        for x in self.__dict__.keys():
            self.x.disable()

class Color(object):
    base = '\033['
    end = '\033[0m'

    def __init__(self, color):
        self.color = color
        self.is_bolded = 0
        self.is_disabled = False
        self.__format_color__()

    def __format_color__(self):
        self.color_str = '%s%s%s' % (Color.base, self.is_bolded, self.color)

    def bold(self):
        self.is_bolded = 1
        self.__format_color__()
        return self
       
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

        return '%s%s%s%s%s' % (beginning, self.color_str, colored, Color.end, end)

    def __repr__(self):
        return '' if is_disabled else self.color_str
