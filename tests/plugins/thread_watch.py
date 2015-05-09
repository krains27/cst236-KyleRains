import sys
import threading
from nose2.events import Plugin

__unittest = True


class ThreadWatch(Plugin):
    configSection = 'thread-watch'

    def __init__(self):
        self.file_hndl = open('ThreadReport.txt', 'w')
        self.curr_test = None
        self._trace = None

    def write_file(self, msg):
        self.file_hndl.write(msg)
        self.file_hndl.write('\n')
        self.file_hndl.flush()

    def startTest(self, event):
        try:
            self.threads = threading.enumerate()
            self.curr_test = event.test
        except Exception as Ex:
            self.write_file(Ex.message)

    def stopTest(self, event):
        try:
            for t in threading.enumerate():
                if t not in self.threads:
                    self.write_file('Test {0} left {1} open'.format(self.curr_test, t.name))
        except Exception as Ex:
            self.write_file(Ex.message)

    def stopTestRun(self, event):
        self.file_hndl.close()