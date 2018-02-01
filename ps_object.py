

from abc import ABCMeta

import re


class TFExercise():
    __metaclass__ = ABCMeta

    def info(self):
        return self.__class__.__name__

class DataStorageManager(TFExercise):
    """ 建模 """

    def __init__(self, path_to_file):
        with open(self, path_to_file) as f:
            self._data = f.read()
        pattern = re.compile('[\W_]+')
        self._data = pattern.sub(' ', self._data).lower()

    def words(self):
        return self._data.split()

    def info(self):
        return super(DataStorageManager, self).info() + ": My major data" \
                                                        "structure is a" \
                                                    + self._data.__class__.__name__



