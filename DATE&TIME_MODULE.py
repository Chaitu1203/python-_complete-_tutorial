
import datetime
import time
#time module:the time module consists of all time related function that are required to perform various operations using time .
#time module  begains recording time from the epoch (epoch means time in history and it begains at 1st jan 1970)
"""
function ()                                                        discription()
time()                                    |       returns the number of seconds 
time.ctime()                              |       returns the current date and time
localtime()                               |       return the date&time in time.struct format
time.mktime()                             |       returns the seconds passed since epoch pass Output  
time.asctime()                            |       returns a string represnting the same
"""
time.time() 
#this method returns the number of seconds that have passed since the epoch
#2 ctime
time.ctime(1665487876.386084)
#returns the current date and time

help(time.ctime)
#its helps the what time of time function it is

# localtime
#return the date&time in time.struct format
"""struct time means
attribute   |                                          | values
tm_year     |  starting from year 0000 ==> 9999        |0000..,2022..,9999
tm_month    |       month                              |1--12
tm_mday     |     days in a month                      |1--31
tm_hour     |     hours in a day                       |0--23
tm_min      |      mintues in a hour                   | 0--59
tm_sec      |       seconds in a mintues               |0--61
tm_wday     |     week days                            |0-6 (where 0 starts with monday)
tm_yday     |      year days                           |1-366
tm_isdst    | day light saving time                    |0,1,-1 (0ifnot,1 summer, -1unknown)
"""
# now run localtime its gives clarity
time.localtime()

#mktime (returns the seconds passed since epoch pass output)
a = time.localtime()
b = time.mktime(a)
print(b)

#asctime (returns the string representing the same)
# currrent time from the struct time method format return it local format you can make you asctime method
a = time.localtime() # struct format
b = time.asctime(a)    #turns to local format
print(b)  

"""strftime: This method returns a string representing date and time using date, time or datetime object.
    Commonly used format codes:
    
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM."""

x = time.strftime("%d/%m/%Y")
print(x)

#using (time.strptime) converts into struct time method
x = "11 october 2022"
y = time.strptime(x,"%d %B %Y")
print(y)


##DATE TIME MODULE
"""
function()                     discription()
datetime()             |     datetime constructor
datetime.today()       |     returns current date&time
datetime.now()         |       returns current date&time
date()                  |      take year,month and day as a parameter and creates the corresponding date
time()                 |       takes hour,min,sec,microseconds and tzinfo as parameter and cretes the corresponding data
datetime.fromstamp()     |      converts seconds to reeturn the corrersponding date & time
time.delta             |        it is the differnce b/w different dates (or) times durartion"""
#datetime:datetime constructor
print(datetime.datetime(2022,10,11,18,36,54,256))

#datetime.today(its returns current date&time)
datetime.datetime.today()

#datetime.now(its returns current date&time)
datetime.datetime.now()

v = datetime.datetime.now()
v.year
v.month
v.time
v.day

#date(take year,month and day as a parameter and creates the corresponding date)

x = datetime.date(2022,10,12)
print(x)

#time (takes hour,min,sec,microseconds and tzinfo as parameter and cretes the corresponding data)

x = datetime.time( 6,36,23,)
print(x)


#TIME_DELTA
#this method represents duration which can either be the sum (or) the difference b/w two differnt dates
b1 = datetime.timedelta(days=20)
b2 = datetime.timedelta(days=31)
b3 = b1-b2
print(b3)
print(type(b3))
# you can use years,min,hours anything
