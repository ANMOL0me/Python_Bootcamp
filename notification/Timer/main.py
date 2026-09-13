from notifypy import Notify
import time
sethour = int(input("hour:"))
setmin = int(input("minute:"))
setsec = int(input("second:"))

hour = 0
sec = 0
minu = 0
while True:
    sec+=1
    if sec>=60:
        sec=0
        minu+=1
        if minu>=60:
            minu=0
            hour+=1
            if hour>=24:
                hour=0

    if(hour<10 and minu<10):
        if(sec<10):
            result = f"0{hour}:0{minu}:0{sec}"
        else:
            result=f"0{hour}:0{minu}:{sec}"
    elif(hour<10 and minu>10):
        if sec<10:
            result=f"0{hour}:{minu}:0{sec}"
        else:
            result=f"0{hour}:{minu}:{sec}"
    else:
        result=f"{hour}:{minu}:{sec}"
    time.sleep(0.9)
    print(result)
    if(sethour==hour and setmin==minu and setsec==sec):
        
        notification = Notify()  
        notification.title="Timer Stop"
        notification.message=f"Time ends\n{result}"
        notification.send()
        break