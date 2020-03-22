from live_tracker import currentStat
from database import dbconnect
from slacker import Slacker
import time
from datetime import datetime

slack = Slacker('xoxb-1003798978883-1017500189990-C6pdaXQ4XTng6hgPsgJ8PPL4')

def hourlynotifier():
    prev_indian = 0
    prev_cured  = 0
    prev_died   = 0
    db = dbconnect()
    if db.exception:
        print "Failed to Connect to Database Module"
        return
    while True:
        try:
            current_status = currentStat()
            current_stat   = current_status.getCurrentStatus()
            now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            if current_status.exception_occrd:
                print "Encountered Exception"
                slack.chat.post_message("@gotubose","Encountered Exception")
                break;
            if current_stat is not None and len(current_stat)>0:
                if current_stat[0] > prev_indian or current_stat[1] > prev_cured or current_stat[2] > prev_died:
                    message = 'NEW STATISTICS :-> Affected : ' + str(current_stat[0]) + ' Cured : ' + str(current_stat[1]) + ' Died : ' + str(current_stat[2])
                    slack.chat.post_message("@gotubose", message)
                    db.insert_into_db((now, current_stat[0], current_stat[1], current_stat[2]))
                    prev_indian, prev_cured, prev_died = current_stat
                    if db.exception:
                        print "Exception Occured in Insertion"
                        raise Exception("Exception Occured in Database Module")
                else:
                    print "Last Checked at ",now

            time.sleep(12)
        except:
            slack.chat.post_message("@gotubose", message)
            break;


if __name__ == '__main__':
    hourlynotifier()
