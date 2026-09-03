from uuid import uuid4
from datetime import datetime
from time import sleep

UUID = uuid4()

while True:
    current_time = datetime.now()
    print(f"{datetime.isoformat(current_time)}Z: {UUID}")
    sleep(5)