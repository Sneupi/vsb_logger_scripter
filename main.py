"""
CLI-based serial hardware logging and scripting tool.
Originally made for Sion Power Corporation's Voltage Sense & Balancing (VSB) board testing.
Program is hardware agnostic, for reusability.
"""
from logger import Logger
from threading import Thread, Event
import time
try:
    from init import ser, log_path
except Exception as e:
    print(f"\033[91m[INIT ERR]\033[0m {e}")
    exit(1)

log = Logger(log_path)
run_event = Event()

def rx_thread():
    """Waits for read and logs"""
    while run_event.is_set():
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            print(data)
            log.log(('RX',data))
        else:
            time.sleep(0.025)

def tx_thread():
    """Waits for write and logs"""
    while True:
        try:
            data = input().strip()
            ser.write(data.encode() + b'\n')
            print(data.strip())
            log.log(('TX',data))
        except KeyboardInterrupt:
            run_event.clear()
            break
    
run_event.set()
reader_thread = Thread(target=rx_thread, daemon=True)
reader_thread.start()

tx_thread()

reader_thread.join()
log.close()
ser.close()