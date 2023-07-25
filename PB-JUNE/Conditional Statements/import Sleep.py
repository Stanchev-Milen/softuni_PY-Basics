from datetime import datetime
import time

t1 = datetime.now()
time.sleep(3)
t2 = datetime.now()

print(t1)
print(t2)
print(t1.time())
print(t2.weekday())
print(t1 == t2)
print(t1 != t2)

