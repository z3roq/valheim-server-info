import time as timesleep
from datetime import datetime, date, time, timedelta
 
log_file = "path_to_valheim_log"
target_file = "where_file_is_saved"
 
check_from_past = 15
online_status = 0
players_online = 0
 
today = datetime.today()
date = today.strftime("%m/%d/%Y")
check = today - timedelta(minutes = check_from_past)
 
f = open(log_file)
for c in f:
 if "Connections" in c:
  split_c = c.split(" ")
  if split_c[0] >= date:
   split_time = split_c[1].split(":")
   rowtime = today.replace(hour=int(split_time[0]), minute=int(split_time[1]), second=int(split_time[2]))
   if(check < rowtime):
    online_status = 1
    players_online = split_c[4]
f.close()    
 
 
f2 = open(target_file, "w")
f2.write(str(online_status))
f2.write("|")
f2.write(str(players_online))
f2.write("|")
f2.write(str(today.strftime("%H:%M:%S")))
f2.close()
