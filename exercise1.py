import time
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
seconds = int(time.strftime('%S'))

print(hour,end=":")
print(minute,end=":")
print(seconds)

if(hour>=0 and hour<=11):
    if(minute>=0 and minute<60):
        if(seconds>=0 and seconds<60):
            print("Good Morning Sir!")
elif(hour>=12 and hour<16):
    if(minute>=0 and minute<60):
        if(seconds>=0 and seconds<60):
            print("Good Afternoon Sir!")
else:
    print("Good Night Sir!")                                    