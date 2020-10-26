#!/user/bin/python
import time as ti
import calendar as cal

ticks = ti.time()
print ("Number of ticks since 12:00am, january 1, 1079", ticks)

localtime = ti.localtime(ti.time())
print ("Current local time: ", localtime)

localtime2 = ti.asctime(ti.localtime(ti.time()))
print ("Current formated time:", localtime2)

vlCal = cal.month(2088,1)
print ("The Calendar")
print(vlCal)