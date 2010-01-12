from configuration import Config

class Wrapper(object):
    def __init__(self, config=None, file=None):
        if config:
            self.config = config
        elif file:
            self.config = Config(file)

    def disabled(self):
        self.config.disable()

    def output(self, line):
        print self.config.format(line)
