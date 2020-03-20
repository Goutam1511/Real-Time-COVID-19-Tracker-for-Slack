from changetracker import Changetracker
from slacker import Slacker
import time
from datetime import datetime

slack = Slacker('YOUR_SLACK_API_TOKEN_HERE')

#slack.chat.post_message("@user","Message")
#slack.chat.post_message("#channel","Message")

def hourlynotifier():
    while True:
        now = datetime.now()
        change = Changetracker()
        if change.notification != '' and not None:
            print change.notification
            slack.chat.post_message("@gotubose",change.notification)
        else:
            print "Last Checked at",now.strftime("%m/%d/%Y, %H:%M:%S")
        if not change.exception:
            change.SaveCurrentStatus()
        else:
            print "Encountered Exception"
        time.sleep(1200)

if __name__ == '__main__':
    hourlynotifier()
