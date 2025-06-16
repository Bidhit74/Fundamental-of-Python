# Question 10 :- Implement an exponential backoff strategy that dubbles the wait time between retries, strating from 1 second, but stops after 5 retries

import time

wait_time = 1
max_retries = 5
attemps = 0

while attemps < max_retries:
    print("Attemp :- ", attemps+1, "_wait time :- ", wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attemps +=1

