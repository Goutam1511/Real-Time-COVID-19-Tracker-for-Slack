import json
from os import path
from Scrapy import currentSituation

class Changetracker:
    notification = ''
    current_data = None
    exception    = False

    def __init__(self):
        currentCondition = currentSituation()
        current_data = currentCondition.getCurrentStatus()

        if current_data == None:
            self.exception = True
            print "Data Fetching failed from Scrapy"
        else:
            self.current_data = current_data

        if path.exists('data.json') and current_data != None:
            try:
                with open('data.json') as json_file:
                    previous_data = json.load(json_file)
                    for key in current_data.keys():
                        if key not in previous_data:
                            self.notification = self.notification + 'New State infected : ' + key + '.\n'
                            self.notification = self.notification + 'Status : [' + str(current_data[key][0]) + ' ' + str(current_data[key][1]) + ' ' + str(current_data[key][2]) + ' ' +  str(current_data[key][3]) + '].\n'
                        else:
                            current_indian, current_foreign, current_cured, current_died = current_data[key]
                            prev_indian, prev_foreign, prev_cured, prev_died = previous_data[key]
                            if current_indian != prev_indian:
                                self.notification = self.notification + "New Indian affected at " + key + "\n"
                                if current_indian > prev_indian:
                                    diff = current_indian - prev_indian
                                    self.notification = self.notification + "Rise by : " + str(diff) + "\n"
                                else:
                                    diff = prev_indian - current_indian
                                    self.notification = self.notification + 'Fall by : ' + str(diff) + "\n"
                                self.notification = self.notification + 'Total cases at ' + key + ' : ' + str(current_indian) + "\n"
                            if current_died > prev_died:
                                diff = current_died - prev_died
                                self.notification = self.notification + 'New death at ' + key + ".\n"
                                self.notification = self.notification + 'Rise of death by : ' + str(diff) + ".\n"
                                self.notification = self.notification + 'Total died at ' + key + ' : ' + str(current_died) + "\n"
                            if current_cured > prev_cured:
                                diff = current_cured - prev_cured
                                self.notification = self.notification + str(diff) + ' Cured at ' + key + ".\n"
            except:
                print "Exception occured at Changetracker"
                self.exception = True
        else:
            if current_data != None:
                with open('data.json','w') as outfile:
                    print current_data
                    json.dump(current_data, outfile)
            else:
                self.exception = True

    def SaveCurrentStatus(self):
        with open('data.json','w') as outfile:
            json.dump(self.current_data, outfile)
