print('Please input time')
hour = int(input('hour:'))
minute = int(input('minute:'))
sec = int(input('sec:'))
# print(type(sec))
# if(int(hour)==23 & int(minute)==59 & int(sec)==59):
if(hour == 23 and minute == 59 and sec == 59):
    print("Time after one sec is: 00:00:00")
elif(minute == 59 and sec == 59):
    print("Time after one sec is: %02d:00:00" % (hour+1))
elif(sec == 59):
    print("Time after one sec is: %02d:%02d:00" % (hour, minute+1))
else:
    print("Time after one sec is: %02d:%02d:%02d" % (hour, minute, sec+1))
