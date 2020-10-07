from pynput.keyboard import Controller, Key
import time
import random as ra
k= Controller()
def random():
    r=ra.randint(1,2)
    if r==1:
        k.type('yogi and vishal random for sale 50% off')
    else:
        k.press(Key.enter)
        k.release(Key.enter)
def see():
    k.type('yogi and vishal for sale 50% off')
    k.press(Key.enter)
    k.release(Key.enter)

time.sleep(2.4)
print("wait")
x=0
while x<50:
        time.sleep(0.10)
        # random()
        see()   
        # ass()
        x+=1
print ("yoo")                                                                                 