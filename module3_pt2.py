time_now = int(input("What is the time now (in hours): "))
alarm_wait = int(input("How long should the alarm be set for (in hours): "))
future_time = (time_now + alarm_wait) % 24
print('The alarm will go off at: ' + str(future_time))