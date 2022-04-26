#simple bgt-like timer in python
import time
class timer:
    current = 1
    def restart(self):
        self.current=time.perf_counter()
    def elapsed(self):
        return int((time.perf_counter()-self.current)*1000)