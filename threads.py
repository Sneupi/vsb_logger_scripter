
from logger import Logger
from threading import Event
from serial import Serial
import time

def rx_thread(ser: Serial, log: Logger, run_event: Event):
    """Waits for read and logs"""
    while run_event.is_set():
        try:
            if ser.in_waiting > 0:
                data = ser.readline().decode().strip()
                print(data)
                log.log(('RX',data))
            else:
                time.sleep(0.025)
        except Exception as e:
            print(f"\033[91m[RX ERR]\033[0m {e}")
            
def tx_thread(ser: Serial, log: Logger, run_event: Event):
    """Waits for write and logs"""
    while run_event.is_set():
        try:
            data = input().strip()
            ser.write(data.encode() + b'\n')
            print(data.strip())
            log.log(('TX',data))
        except EOFError:
            pass
        except Exception as e:
            print(f"\033[91m[TX ERR]\033[0m {e}")