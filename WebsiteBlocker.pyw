import time
from datetime import datetime as dt

hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
#hosts_path=r"hosts"
redirect="127.0.0.1"

website_list=["www.youtube.com","youtube.com"]
hour_timings=[(8,16),(8,16)]
while True:
    with open(hosts_path,"r+") as file:
        content=file.read()
        add=[]
        remove=[]
        for hours, website in zip(hour_timings,website_list):
            if dt(dt.now().year,dt.now().month,dt.now().day,hours[0]) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,hours[1]):
                if website not in content:
                    add.append(website)
            else:
                remove.append(website)

        file.seek(0)
        lines=file.readlines();
        file.seek(0)
        for line in lines:
            if not any (website in line for website in remove):
                file.write(line)

        file.truncate()
        for website in add:
            file.write(redirect +" " +website+"\n")

    time.sleep(5)
