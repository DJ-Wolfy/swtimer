#let's test the python timer script
import swtimer
testtimer=swtimer.timer()
while True:
    if testtimer.elapsed()>1000:
        testtimer.restart()
        print("tick")
