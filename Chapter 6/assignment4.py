import os
import sys


class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        if not os.path.isfile(self._filename):
            try:
                open(self._filename, 'w').close()
            except IOError:
                raise IOError('arg to ConfigDict must be a valid pathname')
        with open(self._filename) as fh:
            for line in fh:
                line = line.rstrip()
                k, v = line.split('=', 1)
                super().__setitem__(k, v)

    def __setitem__(self, k, v):
        super().__setitem__(k, v)
        with open(self._filename, 'w') as fh:
            for key, value in self.items():
                fh.write('{0}={1}\n'.format(key, value))

    def __getitem__(self, key):
        if key not in self:
            raise ConfigKeyError(self, key)
        return super().__getitem__(key)


class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        return 'key {0} not found.  Available keys: ({1})'.format(self.key, ', '.join(self.keys))