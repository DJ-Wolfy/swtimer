##swtimer
###what's this?
This is a very, very simple script that can help you to make timers a lot faster.
An example is included in timer_example.py
###what does it support?
It's very simple, first you must instantiate a class object
timertest=swtimer.timer()
Then, we can restart it,
timertest.restart()
and check it
if timertest.elapsed()>500:

This is millisecond accurate
###notes
This uses the builtin time module in python
###licensing
This is unlicensed, though if you want to credit me, you can.
###coming soon
I'm going to add a pause function to this in the next few days, so stay tuned for that.

Note: This code is no longer being maintained. Please see the WolfGames engine
