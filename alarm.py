import sys
import time

if len(sys.argv) > 1:
    py_file, seconds = sys.argv[:2]
else:
    seconds: int = 1
    
try:
    print(f"alarm after {seconds} seconds")
    time.sleep(int(seconds))
    while True:
        print("alarm!", '\a')  # \a is ASCII character nummer 07 (BELL)
        time.sleep(0.75)
except KeyboardInterrupt:  # CTRL + C
    print("stop alarm")
    pass