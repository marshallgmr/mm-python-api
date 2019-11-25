 ##################################################
## Axis Configuration
##################################################
## Version: 1.6.8
## Email: info@vention.cc
## Status: tested
##################################################

import sys, os

#Adds mm-python-api to the sys path so that we can access MachineMotion.py 
import configWizard

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir)
from _MachineMotion import *

enableDebug = False
# Define a callback to process controller gCode responses if desired. This is mostly used for debugging purposes.
def debug(data):
    if(enableDebug): print("Debug Message: " + data + "\n")

mm = MachineMotion(debug, DEFAULT_IP_ADDRESS.usb_windows)

cw = configWizard.configWizard()
try:
    config = cw.getSavedConfigs(mm)
except cw.userQuit:
    pass
cw.userQuit()


print(config)