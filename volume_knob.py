#!/usr/bin/python

from gpiozero import Button, RotaryEncoder
import alsaaudio
import subprocess

mute = Button(14,pull_up=True) 

encoder = RotaryEncoder(16,15,max_steps=25)
m = alsaaudio.Mixer('PCM')
existingvol = 0

def vol_up():
    vol = m.getvolume()   
    vol = int(vol[0])
    vol = vol + 1
    if vol >= 100:
       vol = 100
    # m.setvolume(vol)
    subprocess.call(['amixer',  'set', 'PCM', '4%+'])
def vol_down():     
    vol = m.getvolume()   
    vol = int(vol[0])
    vol = vol - 1
    if vol <= 0:
       vol = 0
    # m.setvolume(vol)
    subprocess.call(['amixer',  'set', 'PCM', '4%-'])
def vol_mute():
    vol = m.getvolume()   
    vol = int(vol[0])
    if vol > 0:
        #print("Mute")
        change_storedvol(vol)
        vol = 0
    else:
        vol = existingvol
        # m.setvolume(vol)
    subprocess.call(['amixer',  'set', 'PCM', f"{vol}%"], shell=True)
mute.when_pressed = vol_mute
encoder.when_rotated_counter_clockwise = vol_down
encoder.when_rotated_clockwise = vol_up
def change_storedvol(currVol):
    global existingvol
    existingvol = currVol 
# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting")