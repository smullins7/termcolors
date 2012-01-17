
from optparse import OptionParser
import re
import sys
import traceback

from termcolors.color import foreground_colors

regexes = {}
last = None
def read_config(filename=None):
    try:
        filename = filename or '/etc/termcolors.rc'
        global regexes
        for line in open(filename):
            regex, sep, field_colors = eval(line)
            #regex, sep, field_colors = eval('"""' + line + '"""')
            regexes[re.compile(regex)] = (sep, [foreground_colors[color]
                    for color in field_colors])

    except Exception, e:
        print "Error opening config file %s" % filename
        print traceback.print_exc(e)

def handle_input(fp):
    try:
        while not fp.closed:
            line = fp.readline()
            if not line:
                break
            line = line.strip()
            print colorize(line)
    except KeyboardInterrupt:
        pass

def colorize(line):
    global regexes
    global last
    for pattern in regexes:
        match = pattern.match(line)
        if not match:
            continue

        sep, colors = regexes[pattern]
        fields = line.split(sep)
        line_buffer = []
        for text, color in zip(fields, colors):
            line_buffer.append(color.colorize(text))

        last = color
        return sep.join(line_buffer)

    if last:
        return last.colorize(line)

    return line

if __name__ == "__main__":
    parser = OptionParser()

    parser.add_option('-f', '--file', help='open file to read input')
    parser.add_option('-c', '--config', help='configuration file override')

    opts, args = parser.parse_args()

    read_config(opts.config)
    fp = open(opts.file) if opts.file else sys.stdin
    handle_input(fp)
