import os
import pickle


class ConfigPickleDict(dict):

    config_dir = '.'

    def __init__(self, picklename):
        self._filename = os.path.join(ConfigPickleDict.config_dir, picklename + '.pickle')
        if not os.path.isfile(self._filename):
            with open(self._filename, 'w') as fh:
                pickle.dump({}, fh)
        with open(self._filename) as fh:
            pkl = pickle.load(fh)
            self.update(pkl)

    def __setitem__(self, k, v):
        super().__setitem__(k, v)
        with open(self._filename, 'w') as fh:
            pickle.dump(self, fh)

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