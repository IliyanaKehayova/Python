import time

#for count in range(5):
    #print(time.ctime())
    # Prints the current time with a five second difference
    #time.sleep(5)


my_time = int(input("Enter number in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")

