import time

#for count in range(5):
    #print(time.ctime())
    # Prints the current time with a five second difference
    #time.sleep(5)


my_time = int(input("Enter number on seconds: "))

for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)

print("Time's up!")

