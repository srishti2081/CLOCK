second=55
minute=59
hour=3

import time 

from turtle import *
setup()
t1 = Turtle()

while True:
    t1.clear()
    t1.write(str(hour).zfill(2) + ":" +str(minute).zfill(2) + ":" +str(second).zfill(2),font=("arial",30,"normal"))
    second = second+1
    time.sleep(1)
    if second==60:
        second=0
        minute=minute+1
    if minute==60:
       minute=0
       hour=hour +1
