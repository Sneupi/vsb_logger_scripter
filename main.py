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
from threads import rx_thread, tx_thread
try:
    from init import ser, log_path
except Exception as e:
    print(f"\033[91m[INIT ERR]\033[0m {e}")
    exit(1)

log = Logger(log_path)
run_event = Event()

run_event.set()
reader_thread = Thread(target=rx_thread, args=(ser, log, run_event), daemon=True)
reader_thread.start()

writer_thread = Thread(target=tx_thread, args=(ser, log, run_event), daemon=True)
writer_thread.start()

# block main until keyboard interrupt
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        # signal threads to stop
        run_event.clear()
        break

# wait on threads to finish
writer_thread.join()
reader_thread.join()

log.close()
ser.close()