import time
from datetime import datetime as dt

web_list = ["www.facebook.com","facebook.com","www.youtube.com","youtube.com","google.com"]

host_path = r"/etc/hosts"
temp = r"hosts"
redirect = "127.0.0.1"

while True:
    if dt.now().weekday()<=4:
        if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
                print("Working Hours",dt.now())
                with open(host_path,'r+') as file:
                    content = file.read()
                    for web in web_list:
                        if web in content:
                            pass
                        else:
                            file.write(redirect + " "+ web+ "\n")
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (web in line for web in web_list):
                    file.write(line)
            file.truncate()
        print("FUN HOURS...",dt.now())
    time.sleep(1)






