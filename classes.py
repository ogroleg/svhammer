# coding: utf-8
import threading


class StoppableThread(threading.Thread):
    def __init__(self, **kwargs):
        super(StoppableThread, self).__init__(**kwargs)
        self._stop = threading.Event()
        self.target = kwargs['target']
        self.kwargs = kwargs.get('kwargs', dict())

    def run(self):
        self.target(stopped=self.stopped, **self.kwargs)

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()
