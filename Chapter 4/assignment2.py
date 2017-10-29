import datetime as dt
import abc

class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def write(self, message):
        """ Writes the message to a file"""
        return

    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.write(text + '\n')
        fh.close()


class LogFile(WriteFile):
    def write(self, message):
        dt_str = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.write_line('{0}    {1}'.format(dt_str, message))


class DelimFile(WriteFile):
    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, message):
        line = self.delim.join(message)
        self.write_line(line)
