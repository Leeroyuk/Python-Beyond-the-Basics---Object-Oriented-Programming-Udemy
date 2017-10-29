import datetime as dt


class WriteFile(object):

    def __init__(self, filename, writer):
        self.fh = open(filename, 'w')
        self.formatter = writer()

    def write(self, message):
        self.fh.write(self.formatter.format(message))
        self.fh.write('\n')

    def close(self):
        self.fh.close()


class CSVFormatter(object):

    def __init__(self):
        self.delim = ','

    def format(self, this_list):
        new_list = []
        for element in this_list:
            if self.delim in element:
                new_list.append('"{0}"'.format(element))
            else:
                new_list.append(element)
        return self.delim.join(new_list)


class LogFormatter(object):

    def format(self, this_line):
        dt_str = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
        return '{0}    {1}'.format(dt_str, this_line)
