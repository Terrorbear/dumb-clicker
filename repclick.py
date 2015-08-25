#! /usr/bin/python
from pymouse import PyMouse, PyMouseEvent
from time import sleep

CLICKS_PER_SEC = 300
DURATION_SEC = 30
REPEATS = DURATION_SEC * CLICKS_PER_SEC

class RepClick(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
        self.mouse = PyMouse()
        self.first = True

    def click(self, x, y, button, press):
        if self.first and button == 1 and press:
            self.first = False
            x,y = self.mouse.position()
            delay = 1.0/CLICKS_PER_SEC
            for i in xrange(REPEATS):
                self.mouse.click(x, y)
                sleep(delay)
        self.stop()

RepClick().run()
