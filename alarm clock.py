from playsound import playsound
import time
import datetime

def run_alarm(hour, minute, second): #Calculates the amount of time remaining until the set alarm time
    global mainLoop, hour_remaining,second_remaining, minute_remaining
    current_time = datetime.datetime.now()
    if current_time.hour > hour or current_time.minute > minute:
        hour_remaining = hour + 24
        minute_remaining =  minute      
        second_remaining =  second 
    else:
        hour_remaining = abs(current_time.hour - hour)
        minute_remaining = abs(current_time.minute - minute)    
        second_remaining = abs(current_time.second - second )
    
    mainLoop = True
    print(f"The time now is {current_time}")
    print(f"The Alarm is set to go off in {hour_remaining} hours {minute_remaining} minutes and {second_remaining} seconds")
def alarm_time(hour=0, minute=0, second=0, amorpm=1): #sets the alarm
    remaining_seconds = second % 60
    minute += second // 60
    second = remaining_seconds
    remaining_minutes =  minute % 60
    hour += minute // 60
    minute = remaining_minutes
    if amorpm == 2:
        hour += 12
    run_alarm(hour, minute, second)


mainLoop = False
hour = int(input("Alarm Hour: "))
minute= int(input("Alarm Minute: "))
seconds = int(input("Alarm Seconds: "))
amorpm = int(input("1 for AM and 2 for PM: "))

alarm_time(hour,minute,seconds,amorpm)

while mainLoop == True: #Clock function for alarm
    time.sleep(1)
    second_remaining -= 1
    if second_remaining == 0:
        if minute_remaining > 0:
            minute_remaining -=1
            second_remaining += 60
        if minute_remaining == 0 and hour_remaining > 0:
            hour_remaining -= 1
            minute_remaining += 60
            second_remaining += 60
    if hour_remaining == 0 and minute_remaining == 0 and second_remaining == 0:
        playsound(r"C:\Users\kimiw\Downloads\999-social-credit-siren.mp3")
        print("ALARM COMPLETE")
        mainLoop = False

    print(f"Time remaing: {hour_remaining} hours, {minute_remaining} minutes, {second_remaining} seconds")


        

