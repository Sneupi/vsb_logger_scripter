"""
Get required variables to start program from command line args
"""

import serial
import sys
import os

# module variables we need
__all__ = ['ser', 'log_path']

# get arg strings
try:
    port = sys.argv[1]
    baud = sys.argv[2]
    log_path = sys.argv[3]
except IndexError:
    raise IndexError('Usage: python main.py port baud logfile')

# attempt to open the serial port
try:
    ser = serial.Serial(port, baud)
except serial.SerialException:
    raise serial.SerialException(f'Couldn\'t open port {port.upper()} at baud {baud.upper()}.')

# check log path
if not os.path.exists(log_path):
    raise FileNotFoundError(f'Log file does not exist: {log_path}')
elif not log_path.endswith(('.csv', '.txt')):
    raise OSError(f'Log file must end in .csv or .txt: {log_path}')