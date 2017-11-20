import os
import sys


class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
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


if __name__ == "__main__":
    cd = ConfigDict('config.txt')

    if len(sys.argv) == 3:

        key = sys.argv[1]
        value = sys.argv[2]
        print('writing data:  {0}, {1}'.format(key, value))

        cd[key] = value

    else:

        print('reading data')
        for key in cd.keys():
            print('   {0} = {1}'.format(key, cd[key]))