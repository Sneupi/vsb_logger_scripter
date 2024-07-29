"""
CLI-based serial hardware logging and tool.
Program is hardware agnostic, for reusability.

Originally made to run underneath an input scripter
for testing of Sion Power Corporation's 
Voltage Sense & Balancing (VSB) board testing.
"""

from logger import Logger
from threading import Thread, Event
import time
from threads import serial_thread
from queue import Queue
import init
from serial import Serial
from gui.maingui import MainGUI

port, baud, log_path = init.get_args()

ser = Serial(port, baud, timeout=1)
tx_queue = Queue()
log = Logger(log_path)
run_serial = Event()

run_serial.set()
ser_thread = Thread(target=serial_thread, args=(ser, log, run_serial, tx_queue), daemon=True)
ser_thread.start()

gui = MainGUI()
gui.set_send_func(lambda event: tx_queue.put(gui.get_cli_entry()))
gui.mainloop()  # Blocking

run_serial.clear()

ser_thread.join()
log.close()
ser.close()