from configuration import Config

class Wrapper(object):
    def __init__(self, config):
        self.config = config

    def output(self, line):
        print self.config.format(line)
