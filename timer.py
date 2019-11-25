from datetime import datetime
import time

while datetime.now().second != 0:
    time.sleep(1)
    print('sleepin')
