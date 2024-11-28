import datetime

current_time = str(hash(datetime.datetime.now()))
new_time = str(current_time[1:9])

print(len(new_time))
print(new_time)
