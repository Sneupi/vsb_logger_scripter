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
try:
    from init import ser, log_path
except Exception as e:
    print(f"\033[91m[INIT ERR]\033[0m {e}")
    exit(1)

tx_queue = Queue()
log = Logger(log_path)
run_serial = Event()

run_serial.set()
ser_thread = Thread(target=serial_thread, args=(ser, log, run_serial, tx_queue), daemon=True)
ser_thread.start()

# block main until keyboard interrupt
while True:
    try:
        tx_queue.put(input())
    except KeyboardInterrupt:
        # signal threads to stop
        run_serial.clear()
        break

ser_thread.join()
log.close()
ser.close()