# valheim-server-info
Get info from server logs and save it to file. 

This is literally my first python project so be easy on it. 

This creates a file based on valheim server's log file.
It reads server log to see if there is specific line added in past 15 minutes and if yes, fetch data from that line and print them out to a file and also indicate that server is online. It is very easy to add it from file to website if you are running both, valheim and webserver on same machine. There is PHP example included.

I used crontab to run python file for every minute.
