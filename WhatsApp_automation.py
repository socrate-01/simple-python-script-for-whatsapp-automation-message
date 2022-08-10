import pywhatkit
number = input("Please enter the number you wanna send message : ")
number = str(number)
message = input("Please enter the message you wanna send :  ")
message = str(message)
hour = input("Please enter the hour you wanna send this message (ex : 17) :  ")
hour = int(hour)
minute= input("Please enter the minute you wanna send this message (ex : 25) :  ")
#like 17:25

minute = int(minute)
pywhatkit.sendwhatmsg(number,message,hour,minute)
