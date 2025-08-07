import time
wait_time=1
max_retry=5
attempts=0

while attempts < max_retry:
    print(f"attempt {attempts+1} wait time is {wait_time} ")
    time.sleep(wait_time)
    wait_time*=2
    attempts += 1
